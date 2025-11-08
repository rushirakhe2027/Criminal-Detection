import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MongoDB Configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = 'CriminalDetection'
    COLLECTION_NAME = 'CriminalDetails'
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
    
    # Upload Configuration
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
