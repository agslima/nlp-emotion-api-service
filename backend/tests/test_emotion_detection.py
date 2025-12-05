"""
Unit tests for the EmotionDetection package.

This module contains the test suite for the emotion_detector function,
verifying that the correct dominant emotion is returned for specific
text inputs.
"""

import unittest
import json  # Mock test
from unittest.mock import patch  # Mock test
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test class for the EmotionDetection package.
    """

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        """
        Test the emotion_detector function by mocking the API response.
        """

        # Helper function to configure the mock behavior for both .json() and .text
        def configure_mock(mock_obj, data):
            mock_obj.return_value.status_code = 200
            # If the code calls response.json()
            mock_obj.return_value.json.return_value = data
            # If the code calls json.loads(response.text)
            mock_obj.return_value.text = json.dumps(data)

        # 1. Test for JOY
        mock_response_joy = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "joy": 0.99,
                        "sadness": 0.01,
                        "anger": 0.01,
                        "fear": 0.01,
                        "disgust": 0.01,
                    }
                }
            ]
        }
        configure_mock(mock_post, mock_response_joy)

        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy["dominant_emotion"], "joy")

        # 2. Test for ANGER
        mock_response_anger = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "joy": 0.01,
                        "sadness": 0.01,
                        "anger": 0.99,
                        "fear": 0.01,
                        "disgust": 0.01,
                    }
                }
            ]
        }
        configure_mock(mock_post, mock_response_anger)

        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger["dominant_emotion"], "anger")

        # 3. Test for DISGUST
        mock_response_disgust = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "joy": 0.01,
                        "sadness": 0.01,
                        "anger": 0.01,
                        "fear": 0.01,
                        "disgust": 0.99,
                    }
                }
            ]
        }
        configure_mock(mock_post, mock_response_disgust)

        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_disgust["dominant_emotion"], "disgust")

        # 4. Test for SADNESS
        mock_response_sadness = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "joy": 0.01,
                        "sadness": 0.99,
                        "anger": 0.01,
                        "fear": 0.01,
                        "disgust": 0.01,
                    }
                }
            ]
        }
        configure_mock(mock_post, mock_response_sadness)

        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(result_sadness["dominant_emotion"], "sadness")

        # 5. Test for FEAR
        mock_response_fear = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "joy": 0.01,
                        "sadness": 0.01,
                        "anger": 0.01,
                        "fear": 0.99,
                        "disgust": 0.01,
                    }
                }
            ]
        }
        configure_mock(mock_post, mock_response_fear)

        result_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_fear["dominant_emotion"], "fear")

    # def test_emotion_detector(self):
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
