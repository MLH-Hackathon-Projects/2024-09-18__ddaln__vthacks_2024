from datetime import datetime

class Incident:
    def __init__(self, user_id: str, user_name: str, incident_title: str, incident_summary: str, severity_score: float, user_phone, location: str):
        self.user_id = user_id
        self.user_name = user_name
        self.incident_title = incident_title
        self.incident_summary = incident_summary
        self.severity_score = severity_score
        self.user_phone = user_phone
        self.location = location
        self.timestamp = datetime.now()

    def get_severity_score(self) -> float:
        return self.severity_score

    def get_location(self) -> str:
        return self.location

    def get_timestamp(self):
        return self.timestamp

    def __str__(self) -> str:
        return f"Incident(ID: {self.user_id}, Title: {self.incident_title}, Severity: {self.severity_score}, Location: {self.location}, Time: {self.timestamp})"

    def __lt__(self, other):
        if self.severity_score != other.severity_score:
            return self.severity_score > other.severity_score

        return self.timestamp < other.timestamp