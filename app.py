from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from config import Config
from database import Database
from face_recognition_utils import FaceRecognitionUtils
from bson import ObjectId

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

# Initialize database
db = Database()

# Initialize face recognition utils
face_utils = FaceRecognitionUtils()

# Create upload folder if it doesn't exist
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            age_input = request.form.get('age')
            gender = request.form.get('gender')
            crime_type = request.form.get('crime_type')
            description = request.form.get('description')
            address = request.form.get('address')
            
            # Handle file upload
            image_url = None
            detected_age = None
            detected_gender = None
            
            if 'image' in request.files:
                file = request.files['image']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"{timestamp}_{filename}"
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)
                    image_url = f"uploads/{filename}"
                    
                    # Perform facial recognition for age detection
                    face_analysis = face_utils.detect_age_from_image(filepath)
                    if face_analysis['success']:
                        detected_age = face_analysis['age']
                        detected_gender = face_analysis['gender']
            
            # Prepare criminal data
            criminal_data = {
                'name': name,
                'age_input': age_input,
                'detected_age': detected_age,
                'gender': gender,
                'detected_gender': detected_gender,
                'crime_type': crime_type,
                'description': description,
                'address': address,
                'image_url': image_url,
                'created_on': datetime.now()
            }
            
            # Insert into database
            criminal_id = db.insert_criminal(criminal_data)
            
            flash(f'Criminal record registered successfully! ID: {criminal_id}', 'success')
            if detected_age:
                flash(f'AI detected age: {detected_age} years, Gender: {detected_gender}', 'info')
            
            return redirect(url_for('view_records'))
            
        except Exception as e:
            flash(f'Error registering criminal: {str(e)}', 'danger')
            return redirect(url_for('register'))
    
    return render_template("register.html")

@app.route("/view-records")
def view_records():
    search_query = request.args.get('search', '')
    
    try:
        if search_query:
            criminals = db.search_criminals(search_query)
        else:
            criminals = db.get_all_criminals()
        
        # Convert ObjectId to string for template
        for criminal in criminals:
            criminal['_id'] = str(criminal['_id'])
        
        stats = db.get_statistics()
        
        return render_template("view_records.html", 
                             criminals=criminals, 
                             search_query=search_query,
                             stats=stats)
    except Exception as e:
        flash(f'Error fetching records: {str(e)}', 'danger')
        return render_template("view_records.html", criminals=[], stats={})

@app.route("/search-by-image", methods=['POST'])
def search_by_image():
    """Search criminals by uploading an image for facial recognition"""
    try:
        if 'search_image' not in request.files:
            flash('No image provided for search', 'warning')
            return redirect(url_for('view_records'))
        
        file = request.files['search_image']
        if file and allowed_file(file.filename):
            # Save temporary file
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            temp_filename = f"search_{timestamp}_{filename}"
            temp_filepath = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
            file.save(temp_filepath)
            
            # Get all criminals from database
            all_criminals = db.get_all_criminals()
            
            matches = []
            for criminal in all_criminals:
                if criminal.get('image_url'):
                    criminal_image_path = os.path.join('static', criminal['image_url'])
                    
                    # Compare faces
                    result = face_utils.compare_faces(temp_filepath, criminal_image_path)
                    
                    if result['success'] and result['match']:
                        criminal['_id'] = str(criminal['_id'])
                        criminal['match_distance'] = result['distance']
                        criminal['match_confidence'] = round((1 - result['distance']) * 100, 2)
                        matches.append(criminal)
            
            # Clean up temp file
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
            
            # Sort by confidence (lower distance = better match)
            matches.sort(key=lambda x: x['match_distance'])
            
            stats = db.get_statistics()
            
            if matches:
                flash(f'Found {len(matches)} matching criminal(s) using facial recognition!', 'success')
            else:
                flash('No matching criminals found in the database', 'info')
            
            return render_template("view_records.html", 
                                 criminals=matches, 
                                 search_query='Image Search',
                                 stats=stats,
                                 image_search=True)
        else:
            flash('Invalid image file', 'danger')
            return redirect(url_for('view_records'))
            
    except Exception as e:
        flash(f'Error during image search: {str(e)}', 'danger')
        return redirect(url_for('view_records'))

@app.route("/criminal/<criminal_id>")
def view_criminal(criminal_id):
    try:
        criminal = db.get_criminal_by_id(criminal_id)
        if criminal:
            criminal['_id'] = str(criminal['_id'])
            return render_template("criminal_detail.html", criminal=criminal)
        else:
            flash('Criminal record not found', 'warning')
            return redirect(url_for('view_records'))
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('view_records'))

@app.route("/delete-criminal/<criminal_id>", methods=['POST'])
def delete_criminal(criminal_id):
    try:
        result = db.delete_criminal(criminal_id)
        if result > 0:
            flash('Criminal record deleted successfully', 'success')
        else:
            flash('Criminal record not found', 'warning')
    except Exception as e:
        flash(f'Error deleting record: {str(e)}', 'danger')
    
    return redirect(url_for('view_records'))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/api/detect-age", methods=['POST'])
def detect_age_api():
    """API endpoint for real-time age detection"""
    try:
        if 'image' not in request.files:
            return jsonify({'success': False, 'error': 'No image provided'})
        
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"temp_{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Detect age
            result = face_utils.detect_age_from_image(filepath)
            
            # Clean up temp file
            if os.path.exists(filepath):
                os.remove(filepath)
            
            return jsonify(result)
        
        return jsonify({'success': False, 'error': 'Invalid file'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
