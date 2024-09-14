import azure.cognitiveservices.speech as speechsdk
from config import SPEECH_KEY, SPEECH_REGION, GEMINI_API
import google.generativeai as genai

genai.configure(api_key=GEMINI_API)


def analyze_emergency_call(transcription):
    prompt = f"""
    Analyze the following 911 emergency call transcription and extract key information for first responders:
    
    Transcription: {transcription}
    
    Please provide a concise summary including:
    1. Nature of emergency
    2. Location
    3. Number of people involved
    4. Any immediate dangers
    5. Any specific resources needed (e.g., ambulance, fire truck)
    
    Format the response as a brief, bullet-point list.
    """
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error during call: {e}")
        return "Error occurred with the call."

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Listening for emergency call...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        transcription = speech_recognition_result.text
        print("Transcription: ", transcription)
        
        print("\nAnalyzing call...")
        analysis = analyze_emergency_call(transcription)
        print("\nKey Information for First Responders:")
        print(analysis)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        print("Speech Recognition canceled.")

if __name__ == "__main__":
    recognize_from_microphone()