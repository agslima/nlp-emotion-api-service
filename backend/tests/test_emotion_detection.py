"""
Unit tests for the EmotionDetection package.

This module contains the test suite for the emotion_detector function,
verifying that the correct dominant emotion is returned for specific
text inputs.
"""

import unittest
import json # Mock test
from unittest.mock import patch # Mock test
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test class for the EmotionDetection package.
    Inherits from unittest.TestCase to provide testing capabilities.
    """

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        """
        Test the emotion_detector function by mocking the API response.
        
        This tests the logic of parsing the response without hitting
        the real server.
        """
        
        # 1. Simulate the API response for "JOY"
        # We mock what the IBM Watson API would return
        mock_response_joy = {
            "emotionPredictions": [{
                "emotion": {
                    "joy": 0.95,
                    "sadness": 0.01,
                    "anger": 0.01,
                    "fear": 0.01,
                    "disgust": 0.01
                }
            }]
        }
        
        # Configure the mock to return success (200) and the JSON above
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = json.dumps(mock_response_joy)

        # Call the function (it uses the mock internally now)
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy['dominant_emotion'], 'joy')

        # 2. Simulate the API response for "ANGER"
        mock_response_anger = {
            "emotionPredictions": [{
                "emotion": {
                    "joy": 0.01,
                    "sadness": 0.01,
                    "anger": 0.95,
                    "fear": 0.01,
                    "disgust": 0.01
                }
            }]
        }
        mock_post.return_value.text = json.dumps(mock_response_anger)
        
        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger['dominant_emotion'], 'anger')
        
        # 3. Simulate the API response for "DISGUST"
        mock_response_disgust = {
            "emotionPredictions": [{
                "emotion": {
                    "joy": 0.01,
                    "sadness": 0.01,
                    "anger": 0.01,
                    "fear": 0.01,
                    "disgust": 0.95
                }
            }]
        }
        mock_post.return_value.text = json.dumps(mock_response_disgust)

        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')

        # 4. Simulate the API response for "SADNESS"
        mock_response_sadness = {
            "emotionPredictions": [{
                "emotion": {
                    "joy": 0.01,
                    "sadness": 0.95,
                    "anger": 0.01,
                    "fear": 0.01,
                    "disgust": 0.01
                }
            }]
        }
        mock_post.return_value.text = json.dumps(mock_response_sadness)

        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')

        # 5. Simulate the API response for "FEAR"
        mock_response_fear = {
            "emotionPredictions": [{
                "emotion": {
                    "joy": 0.01,
                    "sadness": 0.01,
                    "anger": 0.01,
                    "fear": 0.95,
                    "disgust": 0.01
                }
            }]
        }
        mock_post.return_value.text = json.dumps(mock_response_fear)

        result_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

    #def test_emotion_detector(self):
    #    """
    #    Test the emotion_detector function with various sample sentences.
    #    
    #    This test verifies that the system identifies the correct 
    #    'dominant_emotion' for a set of predefined inputs representing 
    #    Joy, Anger, Disgust, Sadness, and Fear.
    #    """
    #    
    #    # Test Case 1: Testing for Joy
    #    result_1 = emotion_detector("I am glad this happened")
    #    self.assertEqual(result_1['dominant_emotion'], 'joy')
    #    # Test Case 2: Testing for Anger
    #    result_2 = emotion_detector("I am really mad about this")
    #    self.assertEqual(result_2['dominant_emotion'], 'anger')
    #
    #    # Test Case 3: Testing for Disgust
    #    result_3 = emotion_detector("I feel disgusted just hearing about this")
    #    self.assertEqual(result_3['dominant_emotion'], 'disgust')
    #
    #    # Test Case 4: Testing for Sadness
    #    result_4 = emotion_detector("I am so sad about this")
    #    self.assertEqual(result_4['dominant_emotion'], 'sadness')
    #
    #    # Test Case 5: Testing for Fear
    #    result_5 = emotion_detector("I am really afraid that this will happen")
    #    self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
