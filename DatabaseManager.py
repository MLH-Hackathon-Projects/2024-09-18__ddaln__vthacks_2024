import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, dotenv_values 
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
        result = self.collection.insert(incident_data)

        incident_id = result.inserted_id

        new_incident = Incident(
            incident_id = incident_id,
            user_name= incident_data['name'],
            incident_title=incident_data['emergency_details'],
            severity_score= -1,
            location= incident_data['l ocation'],
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
            incident_title = incident['emergency_details'],
            severity_score=incident['severity'],
            location = incident['location'],
            timestamp = incident['timestamp'],
            transcribed_call = incident['transcript']
            )

            incident_list.append(new_incident)
        
            
        return incident_list
    
            




    

