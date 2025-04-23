import unittest
import os
from app.db import get_faces
from app.storage import blob_to_image
from deepface import DeepFace

class TestIntegration(unittest.TestCase):
    def test_compare_from_blob(self):
        for face in get_faces():
            path = f"temp/temp_test_{face['id']}.jpg"
            blob_to_image(face['image'], path)
            result = DeepFace.verify("face_database/caro.jpg", path, enforce_detection=False)
            os.remove(path)
            self.assertIsInstance(result['verified'], bool)