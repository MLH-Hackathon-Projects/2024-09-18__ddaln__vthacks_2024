from datetime import datetime
from IncidentQueue import IncidentQueue
from Incident import Incident
import time

incidentq = IncidentQueue()

# Updated incident creation to match new Incident class format
incidents = [
    Incident("001", "Alice", "Small fire in kitchen", 8.5, "Downtown", datetime.now(), "Caller reports a small fire in the kitchen. Smoke visible but contained."),
    Incident("002", "Bob", "Elderly person fallen", 7.0, "Suburb", datetime.now(), "Elderly individual has fallen and can't get up. No visible injuries but assistance needed."),
    Incident("003", "Charlie", "Car crash on highway", 9.0, "Downtown", datetime.now(), "Multiple vehicle collision on the highway. Several injuries reported. Traffic blocked."),
    Incident("004", "Diana", "Home invasion", 9.5, "Suburb", datetime.now(), "Ongoing home invasion. Caller hiding in closet. Suspects still in the house."),
    Incident("005", "Eve", "Forest fire", 9.5, "Forest", datetime.now(), "Large forest fire spotted. Rapidly spreading. Immediate evacuation may be necessary."),
    Incident("006", "Frank", "Heart attack", 8.0, "Suburb", datetime.now(), "Caller's father experiencing severe chest pain. Possible heart attack. Needs immediate medical attention.")
]

for i in range(3):
    incidentq.add_incident(incidents[i])
    print(f'Incident added: {incidents[i]}')
    #time.sleep(1)  

print()
most_dangerous_location = incidentq.get_most_frequent_location()
print(f'Location with most incidents: {most_dangerous_location}')
close_together_incidents = incidentq.get_incidents_at_location(most_dangerous_location)
print(f'Incidents at {most_dangerous_location}: {close_together_incidents}')
print(f'Most severe incident: {incidentq.get_most_severe()}')
print()

for i in range(3,6):
    incidentq.add_incident(incidents[i])
    print(f'Incident added: {incidents[i]}')
    #time.sleep(1)  

print()
most_dangerous_location = incidentq.get_most_frequent_location()
print(f'Location with most incidents: {most_dangerous_location}')
close_together_incidents = incidentq.get_incidents_at_location(most_dangerous_location)
print(f'Incidents at {most_dangerous_location}: {close_together_incidents}')
print(f'Most severe incident: {incidentq.get_most_severe()}')
print()