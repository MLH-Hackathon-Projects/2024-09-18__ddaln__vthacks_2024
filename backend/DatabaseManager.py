import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv 
from datetime import datetime
from Incident import Incident
from bson.objectid import ObjectId
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        load_dotenv()

        self.uri = os.getenv("MONGO_URI")

        if not self.uri:
            raise Exception("MONGO_URI not found in environment variables")
        
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client['Incidents']
        self.collection = self.db['IncidentReports']

    def serialize(self, data):
        # Convert ObjectId and datetime to JSON-compatible formats
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, ObjectId):
                    data[key] = str(value)
                elif isinstance(value, datetime):
                    data[key] = value.isoformat()
        return data

    def fetch_random_user(self):
        try:
            # Fetch a single random document from the collection
            user = self.collection.find_one({"name": "bob"})
            if user:
                return self.serialize(user)
            return None
        except Exception as e:
            raise Exception(f"Error fetching random user: {e}")

    def insert_incident(self,incident_data: dict):
        self.collection.insert_one(incident_data)

        # incident_id = result.inserted_id

        # return new_incident
    
    def get_incident_by_id(self, incident_id: str)->dict:
        incident_document = self.collection.find_one("_id", ObjectId(incident_id))

        incident_document = self.serialize(incident_document)

        return incident_document
    
    def get_incidents_by_feature(self, feature: str) -> list:
        query = {feature: 1}
        relevant_incidents = self.collection.find(query)

        relevant_incidents = list(relevant_incidents)

        incident_list = []

        for incident in relevant_incidents:

            new_incident = self.serialize(incident)

            incident_list.append(new_incident)
        
            
        return incident_list
    
    def clear_database(self):
        self.collection.delete_many({})
        # print(f"Deleted {result.deleted_count} documents from the collection.")
    
    def get_ordered_by_severity(self)->list:
        incidents = self.collection.find()

        incident_list = []

        for incident in incidents:
            # new_incident = Incident(
            # incident_id = incident.get("_id"),
            # user_name= incident['name'],
            # incident_info = incident['emergency_details'],
            # severity_score=incident['severity'],
            # location = incident['location'],
            # timestamp = incident['timestamp'],
            # transcribed_call = incident['transcript']
            # )

            new_incident = self.serialize(incident)

            incident_list.append((incident['severity'], new_incident))

        incident_list.sort()

        result = [incident for _, incident in incident_list]

        return result
    
    def is_empty(self) -> bool:
        return self.collection.count_documents({}) == 0    

    def get_ordered_by_time(self)->list:
        incidents = self.collection.find()

        incident_list = []

        for incident in incidents:
            # new_incident = Incident(
            # incident_id = incident.get("_id"),
            # user_name= incident['name'],
            # incident_info = incident['emergency_details'],
            # severity_score=incident['severity'],
            # location = incident['location'],
            # timestamp = incident['timestamp'],
            # transcribed_call = incident['transcript']
            # )

            new_incident = self.serialize(incident)

            dt: datetime = incident['timestamp']

            incident_list.append((dt, new_incident))

        incident_list.sort()

        result = [incident for _, incident in incident_list]

        return result
            




    

