"""Unit tests for emotion detection."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests for dominant emotion detection."""

    def test_emotions(self):
        """Test several sample inputs."""
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid this will happen": "fear",
        }

        for text, expected_emotion in test_cases.items():
            result = emotion_detector(text)
            self.assertEqual(result["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    unittest.main()