from pymongo import MongoClient
from config import Config
from datetime import datetime

class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.DATABASE_NAME]
        self.collection = self.db[Config.COLLECTION_NAME]
    
    def insert_criminal(self, criminal_data):
        """Insert a new criminal record"""
        criminal_data['created_on'] = datetime.now()
        result = self.collection.insert_one(criminal_data)
        return result.inserted_id
    
    def get_all_criminals(self):
        """Get all criminal records"""
        return list(self.collection.find())
    
    def search_criminals(self, query):
        """Search criminals by name, crime type, or other fields"""
        search_filter = {
            '$or': [
                {'name': {'$regex': query, '$options': 'i'}},
                {'crime_type': {'$regex': query, '$options': 'i'}},
                {'address': {'$regex': query, '$options': 'i'}}
            ]
        }
        return list(self.collection.find(search_filter))
    
    def get_criminal_by_id(self, criminal_id):
        """Get a specific criminal by ID"""
        from bson.objectid import ObjectId
        return self.collection.find_one({'_id': ObjectId(criminal_id)})
    
    def update_criminal(self, criminal_id, update_data):
        """Update a criminal record"""
        from bson.objectid import ObjectId
        update_data['updated_on'] = datetime.now()
        result = self.collection.update_one(
            {'_id': ObjectId(criminal_id)},
            {'$set': update_data}
        )
        return result.modified_count
    
    def delete_criminal(self, criminal_id):
        """Delete a criminal record"""
        from bson.objectid import ObjectId
        result = self.collection.delete_one({'_id': ObjectId(criminal_id)})
        return result.deleted_count
    
    def get_statistics(self):
        """Get database statistics"""
        total_records = self.collection.count_documents({})
        crime_types = self.collection.distinct('crime_type')
        return {
            'total_records': total_records,
            'crime_types': crime_types,
            'crime_type_count': len(crime_types)
        }
