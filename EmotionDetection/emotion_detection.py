import requests 
import json

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Header for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request 
    if response.status_code == 400:
        return {
            'anger' : None, 
            'disgust': None, 
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    formatted_output = json.loads(response.text)
    d = formatted_output['emotionPredictions'][0]['emotion']
    dominant_emotion = max(d, key = d.get)
    d['dominant_emotion'] = dominant_emotion
    return d