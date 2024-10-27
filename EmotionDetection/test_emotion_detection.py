import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        output1 = emotion_detector("I am glad this happened")
        self.assertEqual(output1['dominant_emotion'], 'joy')        
        output2 = emotion_detector("I am really mad about this")
        self.assertEqual(output2['dominant_emotion'], 'anger')        
        output3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(output3['dominant_emotion'], 'disgust')        
        output4 = emotion_detector("I am so sad about this")
        self.assertEqual(output4['dominant_emotion'], 'sadness')        
        output5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(output5['dominant_emotion'], 'fear')        


unittest.main()