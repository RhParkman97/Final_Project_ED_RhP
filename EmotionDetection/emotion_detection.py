#/final_project/Final_Project_ED_RhP/emotion_detection

# Import important libraries 
import json
import requests

def emotion_detector(text_to_analyse):
    """ This function performs emotional detection on input text and
        returns the emotional label and score.
    """
    # Define the URL for the emotion detector API (PEP8 compliant)
    url = (
    'https://sn-watson-emotion.labs.skills.network/v1'
    '/watson.runtime.nlp.v1/NlpService/EmotionPredict'
     )

    # Create the Payload with the text to be analysed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload (myobj) and headers
    response = requests.post(url, json=myobj, headers=header)
     
    formatted_response = json.loads(response.text)

    # Extract emotions and their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
   # Find dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }