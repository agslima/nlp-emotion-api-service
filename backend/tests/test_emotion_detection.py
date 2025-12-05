"""
Unit tests for the EmotionDetection package.

This module contains the test suite for the emotion_detector function,
verifying that the correct dominant emotion is returned for specific
text inputs.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test class for the EmotionDetection package.
    Inherits from unittest.TestCase to provide testing capabilities.
    """

    def test_emotion_detector(self):
        """
        Test the emotion_detector function with various sample sentences.
        
        This test verifies that the system identifies the correct 
        'dominant_emotion' for a set of predefined inputs representing 
        Joy, Anger, Disgust, Sadness, and Fear.
        """
        
        # Test Case 1: Testing for Joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test Case 2: Testing for Anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test Case 3: Testing for Disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test Case 4: Testing for Sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test Case 5: Testing for Fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
