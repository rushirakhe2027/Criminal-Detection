# 🚔 Criminal Detection Bureau

> A comprehensive web-based criminal identification and record management system for law enforcement agencies

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

Criminal Detection Bureau is a modern web application designed for law enforcement agencies to efficiently manage criminal records. The system provides a centralized platform for registering criminals, storing their information securely in MongoDB, and detecting criminals through image uploads.

### ✨ Key Features

- 📝 **Criminal Registration** - Comprehensive form to register criminal records with photos
- 💾 **MongoDB Integration** - Secure and scalable NoSQL database storage
- 🔍 **Detect Criminal** - Upload images for criminal detection (UI ready, backend in development)
- 📊 **Modern UI/UX** - Clean, professional interface with responsive design
- 🔒 **Secure Storage** - File validation and secure data management
- 📱 **Responsive Design** - Works seamlessly on all devices

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Flask 3.0.0, Python 3.8+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Database** | MongoDB |
| **Icons** | Bootstrap Icons |
| **Fonts** | Google Fonts (Inter) |

## 📦 Installation & Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **MongoDB** - [Download MongoDB Compass](https://www.mongodb.com/try/download/compass)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/rushirakhe2027/Criminal-Detection.git
cd Criminal-Detection
```

#### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required Packages:**
- Flask==3.0.0
- pymongo==4.6.0
- python-dotenv==1.0.0
- Werkzeug==3.0.1

#### 4. Set Up MongoDB

1. **Install MongoDB Compass** from the link above
2. **Start MongoDB Service**:
   - Windows: MongoDB starts automatically after installation
   - Linux: `sudo systemctl start mongod`
   - Mac: `brew services start mongodb-community`

3. **Verify Connection**:
   - Open MongoDB Compass
   - Connect to: `mongodb://localhost:27017/`
   - The application will automatically create the database

#### 5. Configure Environment (Optional)

Create a `.env` file in the root directory (optional):

```env
MONGO_URI=mongodb://localhost:27017/
SECRET_KEY=your-secret-key-here
```

If you don't create this file, the application will use default values.

#### 6. Run the Application

```bash
python app.py
```

The application will start on: **http://localhost:5000**

#### 7. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 🚀 Usage Guide

### 1. Register a Criminal

1. Click on **"Criminal Registration"** in the navigation menu
2. Fill in the required information:
   - **Name**: Full name of the criminal
   - **Age**: Age in years
   - **Gender**: Select from dropdown
   - **Crime Type**: Select the type of crime
   - **Description**: Detailed description of the crime
   - **Address**: Complete address
   - **Photo**: Upload a clear photo (JPG, PNG, GIF)
3. Click **"Submit Record"**
4. The record will be saved to MongoDB

### 2. Detect Criminal

1. Click on **"Detect Criminal"** in the navigation menu
2. Upload a photo of the person to identify
3. Preview the image
4. Click **"Detect Criminal"**
5. *(Note: Detection backend is currently in development)*

### 3. View Contact Information

1. Click on **"Contact"** in the navigation menu
2. View the bureau's contact details:
   - **Email**: support@criminaldetection.gov.in
   - **Phone**: +91 00000000
   - **Address**: Pune, Maharashtra, India

## 📊 Database Structure

### MongoDB Configuration

- **Database Name**: `CriminalDetection`
- **Collection Name**: `CriminalDetails`
- **Connection URI**: `mongodb://localhost:27017/`

### Document Schema

Each criminal record is stored as a document:

```javascript
{
  "_id": ObjectId("auto-generated"),
  "name": "String",
  "age_input": "Number",
  "gender": "String",
  "crime_type": "String",
  "description": "String",
  "address": "String",
  "image_url": "String (path to uploaded photo)",
  "created_on": ISODate("timestamp")
}
```

### Viewing Data in MongoDB

1. Open **MongoDB Compass**
2. Connect to `mongodb://localhost:27017/`
3. Navigate to: **DATABASES** → **CriminalDetection** → **CriminalDetails**
4. Click on **"Documents"** tab to view all records

## 📁 Project Structure

```
Criminal-Detection/
│
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── database.py                 # MongoDB operations
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── home.html              # Landing page
│   ├── register.html          # Criminal registration form
│   ├── view_records.html      # Detect criminal page
│   ├── criminal_detail.html   # Individual record view
│   └── contact.html           # Contact information
│
└── static/                     # Static assets
    ├── css/
    │   └── style.css          # Custom styles
    └── uploads/               # Uploaded criminal photos
```

## 🎨 Features in Detail

### Criminal Registration
- Comprehensive form with validation
- Image upload with file type checking
- Real-time image preview
- Automatic timestamp recording
- Direct MongoDB storage

### Detect Criminal
- Clean image upload interface
- Image preview functionality
- User-friendly design
- Ready for AI integration

### Modern UI
- Professional law enforcement theme
- Dark blue, grey, and white color scheme
- Smooth animations and transitions
- Responsive design for all screen sizes
- Bootstrap 5 components

## 🔐 Security Features

- ✅ File upload validation (type and size)
- ✅ Secure filename generation with timestamps
- ✅ Input sanitization
- ✅ MongoDB injection prevention
- ✅ Environment variable support for sensitive data

## 🐛 Troubleshooting

### MongoDB Connection Issues

**Problem**: Cannot connect to MongoDB

**Solution**:
1. Ensure MongoDB service is running
2. Check if port 27017 is available
3. Verify MongoDB Compass can connect to `mongodb://localhost:27017/`

### Port Already in Use

**Problem**: Port 5000 is already in use

**Solution**:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Module Not Found Errors

**Problem**: ImportError or ModuleNotFoundError

**Solution**:
```bash
pip install -r requirements.txt --upgrade
```

## 📝 Development

### Adding New Features

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Test thoroughly

4. Commit and push:
   ```bash
   git add .
   git commit -m "Add your feature description"
   git push origin feature/your-feature-name
   ```

### Running in Debug Mode

The application runs in debug mode by default. To disable:

```python
# In app.py, change:
app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Contact & Support

**Criminal Detection Bureau**

- 📧 **Email**: support@criminaldetection.gov.in
- 📱 **Phone**: +91 00000000
- 📍 **Address**: Pune, Maharashtra, India

## 👨‍💻 Author

**Rushi Rakhe**
- GitHub: [@rushirakhe2027](https://github.com/rushirakhe2027)
- Repository: [Criminal-Detection](https://github.com/rushirakhe2027/Criminal-Detection)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [MongoDB](https://www.mongodb.com/) - Database
- [Bootstrap](https://getbootstrap.com/) - UI framework
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Icon library

## 📈 Future Enhancements

- [ ] AI-powered facial recognition for criminal detection
- [ ] Advanced search filters
- [ ] User authentication and authorization
- [ ] Role-based access control (Admin, Officer, Viewer)
- [ ] Export records to PDF/Excel
- [ ] Dashboard with analytics and statistics
- [ ] Real-time notifications
- [ ] Audit logs and activity tracking

---

<div align="center">
  <strong>Built for Law Enforcement Agencies</strong>
  <br>
  <sub>Powered by Modern Web Technologies</sub>
  <br><br>
  <p>⭐ Star this repository if you find it helpful!</p>
</div>
