import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Required headers
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        
        # Extract emotions and scores
        emotions = result.get("emotionPredictions", [])[0].get("emotion", {})
        
        # Build dictionary with required emotions
        formatted_output = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }
        
        # Find dominant emotion
        dominant_emotion = max(formatted_output, key=formatted_output.get)
        formatted_output["dominant_emotion"] = dominant_emotion
        
        return formatted_output
    else:
        return {"error": f"Request failed with status {response.status_code}"}
