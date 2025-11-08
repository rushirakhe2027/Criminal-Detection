import cv2
import numpy as np
from deepface import DeepFace
from PIL import Image
import os

class FaceRecognitionUtils:
    
    @staticmethod
    def detect_age_from_image(image_path):
        """
        Detect age from an image using DeepFace
        Returns: dict with age, gender, and other attributes
        """
        try:
            # Analyze the image
            analysis = DeepFace.analyze(
                img_path=image_path,
                actions=['age', 'gender', 'race', 'emotion'],
                enforce_detection=False
            )
            
            # Handle both single face and multiple faces
            if isinstance(analysis, list):
                analysis = analysis[0]
            
            return {
                'success': True,
                'age': analysis.get('age', 'Unknown'),
                'gender': analysis.get('dominant_gender', 'Unknown'),
                'race': analysis.get('dominant_race', 'Unknown'),
                'emotion': analysis.get('dominant_emotion', 'Unknown')
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'age': 'Unknown',
                'gender': 'Unknown'
            }
    
    @staticmethod
    def detect_face(image_path):
        """
        Detect if a face exists in the image
        Returns: True if face detected, False otherwise
        """
        try:
            # Load the image
            img = cv2.imread(image_path)
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Load the face cascade
            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
            
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            return len(faces) > 0
        except Exception as e:
            print(f"Face detection error: {e}")
            return False
    
    @staticmethod
    def extract_face_encoding(image_path):
        """
        Extract face encoding for comparison
        Returns: face encoding array
        """
        try:
            # Use DeepFace to extract face representation
            embedding = DeepFace.represent(
                img_path=image_path,
                model_name='VGG-Face',
                enforce_detection=False
            )
            
            if isinstance(embedding, list):
                embedding = embedding[0]
            
            return {
                'success': True,
                'encoding': embedding.get('embedding', [])
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'encoding': []
            }
    
    @staticmethod
    def compare_faces(image_path1, image_path2):
        """
        Compare two faces and return similarity score
        Returns: dict with match result and distance
        """
        try:
            result = DeepFace.verify(
                img1_path=image_path1,
                img2_path=image_path2,
                model_name='VGG-Face',
                enforce_detection=False
            )
            
            return {
                'success': True,
                'match': result.get('verified', False),
                'distance': result.get('distance', 1.0),
                'threshold': result.get('threshold', 0.4)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'match': False
            }
    
    @staticmethod
    def validate_image(image_path):
        """
        Validate if the image is suitable for face recognition
        """
        try:
            # Check if file exists
            if not os.path.exists(image_path):
                return False, "Image file not found"
            
            # Try to open the image
            img = Image.open(image_path)
            
            # Check image format
            if img.format not in ['JPEG', 'PNG', 'JPG']:
                return False, "Invalid image format. Use JPEG or PNG"
            
            # Check image size
            width, height = img.size
            if width < 100 or height < 100:
                return False, "Image too small. Minimum 100x100 pixels required"
            
            return True, "Image is valid"
        except Exception as e:
            return False, f"Image validation error: {str(e)}"
