# Importing libraries 
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        """ This function will test the emotional_detector() by using 
        assertEqual function to check if emotional_detector() output is equal
        to correct output.
        """
        # Test case 1 - I am glad this happened (joy)
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

        # Test case 2 - I am really mad about this (anger)
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

        # Test case 3 - I feel disgusted just hearing about this (disgust)
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

        # Test case 4 - I am sad about this (sadness)
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

        # Test case 5 - I am really afraid that this will happen (fear)
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

unittest.main()