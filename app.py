from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from config import Config
from database import Database
from bson import ObjectId

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

# Initialize database
db = Database()

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
            
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"{timestamp}_{filename}"
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)
                    image_url = f"uploads/{filename}"
            
            # Prepare criminal data
            criminal_data = {
                'name': name,
                'age_input': age_input,
                'gender': gender,
                'crime_type': crime_type,
                'description': description,
                'address': address,
                'image_url': image_url,
                'created_on': datetime.now()
            }
            
            # Insert into database
            criminal_id = db.insert_criminal(criminal_data)
            
            flash(f'Criminal record registered successfully! ID: {criminal_id}', 'success')
            
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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
