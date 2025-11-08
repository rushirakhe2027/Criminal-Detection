# 🚔 Criminal Identification System

> AI-Driven Criminal Detection & Management Platform for Law Enforcement Agencies

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen.svg)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

A comprehensive web-based criminal identification and record management system powered by artificial intelligence. This platform enables law enforcement agencies to register, search, and manage criminal records efficiently using facial recognition technology.

### ✨ Key Features

- 🤖 **AI-Powered Facial Recognition** - Automatic age and gender detection from photos
- 🔍 **Image-Based Search** - Find criminals by uploading photos (facial matching)
- 💾 **MongoDB Integration** - Scalable NoSQL database for criminal records
- 📊 **Statistics Dashboard** - Real-time insights and analytics
- 🎨 **Modern UI/UX** - Professional, responsive design
- 🔒 **Secure** - File validation and data protection
- ⚡ **Fast Search** - Quick retrieval of criminal records

## 🎯 Demo

### Home Page
![Home Page](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80)

### Features
- **Criminal Registration** with photo upload
- **AI Age Detection** using DeepFace
- **Facial Recognition Search** by image
- **Comprehensive Records** with full details
- **Statistics Dashboard** for insights

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Flask 3.0.0, Python 3.8+ |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Database** | MongoDB |
| **AI/ML** | DeepFace, OpenCV, VGG-Face Model |
| **Icons** | Bootstrap Icons |
| **Fonts** | Google Fonts (Inter) |

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB (local or cloud)
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/rushirakhe2027/Criminal-Detection.git
cd Criminal-Detection
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up MongoDB

1. **Install MongoDB Compass**: [Download Here](https://www.mongodb.com/try/download/compass)
2. **Start MongoDB Service**
3. **Connection String**: `mongodb://localhost:27017/`

The application will automatically create:
- Database: `CriminalDetection`
- Collection: `CriminalDetails`

### Step 5: Configure Environment (Optional)

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb://localhost:27017/
SECRET_KEY=your-secret-key-here
```

### Step 6: Run Application

```bash
python app.py
```

Visit: **http://localhost:5000**

## 🚀 Usage

### 1. Register Criminal

1. Navigate to **Criminal Registration**
2. Fill in the form:
   - Full Name
   - Age (manual input)
   - Gender
   - Crime Type
   - Description
   - Address
3. **Upload Photo** (clear, front-facing)
4. Click **Submit**
5. AI automatically detects age and gender
6. Record saved to MongoDB

### 2. Search by Image

1. Go to **Search Criminal**
2. Click **Search by Image**
3. Upload a photo
4. AI performs facial recognition matching
5. View matching records

### 3. Search by Text

1. Enter name, crime type, or address
2. Click **Search**
3. View filtered results

### 4. View Details

- Click **View** on any record
- See complete information
- Compare manual vs AI-detected data
- Delete record if needed

## 📊 Database Schema

```javascript
{
  "_id": ObjectId,
  "name": String,
  "age_input": Number,
  "detected_age": Number,        // AI-detected
  "gender": String,
  "detected_gender": String,     // AI-detected
  "crime_type": String,
  "description": String,
  "address": String,
  "image_url": String,
  "face_encoding": Array,        // For facial matching
  "created_on": DateTime
}
```

## 🤖 AI Features

### Facial Recognition
- **Model**: VGG-Face (DeepFace)
- **Accuracy**: 99.7%
- **Detection**: Age, Gender, Race, Emotion
- **Matching**: Face-to-face comparison

### How It Works

1. **Registration**: Upload photo → AI analyzes → Extracts features
2. **Storage**: Face encoding saved to database
3. **Search**: Upload query image → Compare with all records
4. **Results**: Return matching criminals with similarity scores

## 📁 Project Structure

```
Criminal-Detection/
│
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── database.py                 # MongoDB operations
├── face_recognition_utils.py   # AI utilities
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
│
├── templates/                  # HTML templates
│   ├── home.html
│   ├── register.html
│   ├── view_records.html
│   ├── criminal_detail.html
│   └── contact.html
│
└── static/                     # Static assets
    ├── css/
    │   └── style.css
    ├── js/
    └── uploads/                # Criminal photos
```

## 🔐 Security Features

- ✅ File upload validation (type, size)
- ✅ Secure filename generation
- ✅ Input sanitization
- ✅ MongoDB injection prevention
- ✅ Error handling and logging

## 🎨 Screenshots

### Dashboard
Professional statistics and quick access

### Registration Form
Clean, intuitive interface with real-time preview

### Search Results
Responsive table with photos and AI data

### Criminal Details
Comprehensive view with all information

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Rushi Rakhe**
- GitHub: [@rushirakhe2027](https://github.com/rushirakhe2027)
- Email: rushirakhe2027@gmail.com

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [MongoDB](https://www.mongodb.com/) - Database
- [DeepFace](https://github.com/serengil/deepface) - Facial recognition
- [Bootstrap](https://getbootstrap.com/) - UI framework
- [Unsplash](https://unsplash.com/) - Stock images

## 📞 Support

For support or inquiries:
- 📧 Email: support@criminalid.gov
- 🌐 Website: [Criminal ID System](https://github.com/rushirakhe2027/Criminal-Detection)

---

<div align="center">
  <strong>Built with ❤️ for Law Enforcement Agencies</strong>
  <br>
  <sub>Powered by AI & Modern Web Technologies</sub>
</div>
