from vthacks_2024.backend.speech import recognize_from_microphone
from xgb import xgb_predict
from vthacks_2024.backend.DatabaseManager import DatabaseManager

speech_to_text_dict = recognize_from_microphone()

# print("speech to text dict")
# print(speech_to_text_dict)
# print()

prediction_dict = {
    'age': [speech_to_text_dict['age']],
    'num_people': [speech_to_text_dict['num_people']],
    'mentioned_medical': [speech_to_text_dict['mentioned_medical']],
    'mentioned_violence': [speech_to_text_dict['mentioned_violence']],
    'mentioned_fire': [speech_to_text_dict['mentioned_fire']],
    'mentioned_vehicular': [speech_to_text_dict['mentioned_vehicular']],
    'mentioned_mental_health': [speech_to_text_dict['mentioned_mental_health']],
    'mentioned_natural_disasters': [speech_to_text_dict['mentioned_natural_disasters']],
    'mentioned_environmental_hazards': [speech_to_text_dict['mentioned_environmental_hazards']],
    'mentioned_suspicious_activity': [speech_to_text_dict['mentioned_suspicious_activity']],
    'mentioned_urgency': [speech_to_text_dict['mentioned_urgency']]
}


# print("dict to be used to get severity score")
# print(prediction_dict)
severity_score = float(xgb_predict.predict_severity(prediction_dict))
# print("severity of incident:", severity_score)
# print()

speech_to_text_dict["severity"] = severity_score

# print("document dict to be inserted into db")
# print(speech_to_text_dict)
# print()


dbm = DatabaseManager()
new_incident = dbm.insert_incident(speech_to_text_dict)

print(new_incident)

