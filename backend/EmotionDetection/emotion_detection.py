"""
emotion_detection.py

Module for detecting emotions from text using IBM Watson NLP API.
Provides function `emotion_detector` that returns emotion scores
and the dominant emotion for a given text input.
"""

from typing import Dict
import requests

def emotion_detector(text_to_analyze: str) -> Dict[str, float or None]:
    """
    Detects emotions from a given text using IBM Watson NLP Emotion API.

    Args:
        text_to_analyze (str): Text to analyze for emotions.

    Returns:
        dict: Dictionary containing scores for 'anger', 'disgust', 'fear', 'joy', 'sadness'
              and the 'dominant_emotion'. Returns None values if input is blank or error occurs.
    """

    # Return None values for blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        # Return None values for bad request
        if response.status_code == 400:
            return {k: None for k in ['anger','disgust','fear','joy','sadness','dominant_emotion']}

        response_dict = response.json()

        # Check if 'emotionPredictions' exists and is not empty
        if "emotionPredictions" not in response_dict or not response_dict["emotionPredictions"]:
            return {k: None for k in ['anger','disgust','fear','joy','sadness','dominant_emotion']}

        emotions = response_dict["emotionPredictions"][0]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        result = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }

        return result

    except (requests.RequestException, ValueError, KeyError):
        # Return None values if network/API error occurs or JSON is invalid
        return {k: None for k in ['anger','disgust','fear','joy','sadness','dominant_emotion']}
