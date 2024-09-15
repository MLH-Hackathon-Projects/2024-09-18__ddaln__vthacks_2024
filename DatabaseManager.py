import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv 
from datetime import datetime
from Incident import Incident
from bson.objectid import ObjectId

class DatabaseManager:
    def __init__(self):
        load_dotenv()

        self.uri = os.getenv("MONGO_URI")

        if not self.uri:
            raise Exception("MONGO_URI not found in environment variables")
        
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client['Incidents']
        self.collection = self.db['IncidentReports']

    def insert_incident(self,incident_data: dict)->Incident:
        result = self.collection.insert_one(incident_data)

        incident_id = result.inserted_id

        new_incident = Incident(
            incident_id = incident_id,
            user_name= incident_data['name'],
            incident_info=incident_data['emergency_details'],
            severity_score = incident_data["severity"],
            location= incident_data['location'],
            timestamp = incident_data['timestamp'],
            transcribed_call= incident_data['transcript']
        )

        return new_incident
    
    def get_incident_by_id(self, incident_id: str)->Incident:
        incident_document = self.collection.find_one("_id", ObjectId(incident_id))

        new_incident = Incident(
            incident_id = incident_id,
            user_name= incident_document['name'],
            incident_info = incident_document['emergency_details'],
            severity_score = incident_document['severity'],
            location = incident_document['location'],
            timestamp = incident_document['timestamp'],
            transcribed_call= incident_document['transcript']
        )

        return new_incident
    
    def get_incidents_by_feature(self, feature: str) -> list:
        query = {feature: 1}
        relevant_incidents = self.collection.find(query)

        relevant_incidents = list(relevant_incidents)

        incident_list = []

        for incident in relevant_incidents:
            new_incident = Incident(
            incident_id = incident.get("_id"),
            user_name= incident['name'],
            incident_info = incident['emergency_details'],
            severity_score=incident['severity'],
            location = incident['location'],
            timestamp = incident['timestamp'],
            transcribed_call = incident['transcript']
            )

            incident_list.append(new_incident)
        
            
        return incident_list
    
    def clear_database(self):
        result = self.collection.delete_many({})
        # print(f"Deleted {result.deleted_count} documents from the collection.")
    
    def get_ordered_by_severity(self):
        incidents = self.collection.find()

        incident_list = []

        for incident in incidents:
            new_incident = Incident(
            incident_id = incident.get("_id"),
            user_name= incident['name'],
            incident_info = incident['emergency_details'],
            severity_score=incident['severity'],
            location = incident['location'],
            timestamp = incident['timestamp'],
            transcribed_call = incident['transcript']
            )

            incident_list.append((incident['severity'], new_incident))

        incident_list.sort()

        result = [incident for _, incident in incident_list]

        return result
    
    def is_empty(self) -> bool:
        return self.collection.count_documents({}) == 0    

    def get_ordered_by_time(self):
        incidents = self.collection.find()

        incident_list = []

        for incident in incidents:
            new_incident = Incident(
            incident_id = incident.get("_id"),
            user_name= incident['name'],
            incident_info = incident['emergency_details'],
            severity_score=incident['severity'],
            location = incident['location'],
            timestamp = incident['timestamp'],
            transcribed_call = incident['transcript']
            )

            dt: datetime = incident['timestamp']

            incident_list.append((dt, new_incident))

        incident_list.sort()

        result = [incident for _, incident in incident_list]

        return result
            




    

