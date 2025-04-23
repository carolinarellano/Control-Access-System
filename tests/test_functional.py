# tests/test_functional.py
import unittest
from deepface import DeepFace

class TestCompare(unittest.TestCase):
    def test_compare_same_image(self):
        result = DeepFace.verify("face_database/caro.jpg", "face_database/caro.jpg", enforce_detection=False)
        self.assertTrue(result['verified'])

    def test_compare_different_image(self):
        result = DeepFace.verify("face_database/caro.jpg", "face_database/katy.jpg", enforce_detection=False)
        self.assertTrue(result['verified']) 