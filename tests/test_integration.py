import unittest
import os
from app.db import get_faces
from app.storage import blob_to_image
from deepface import DeepFace

class TestIntegration(unittest.TestCase):
    def test_compare_from_blob_multiple_views(self):
        reference_image = "face_database/caro.jpg"

        for face in get_faces():
            is_caro = face['name'] == "carolinta"

            for view in ["front_image", "right_image", "left_image"]:
                if face.get(view):
                    temp_path = f"temp/temp_test_{face['id']}_{view}.jpg"
                    blob_to_image(face[view], temp_path)

                    result = DeepFace.verify(reference_image, temp_path, enforce_detection=False)
                    os.remove(temp_path)

                    self.assertIsInstance(result['verified'], bool)

                    if is_caro:
                        self.assertTrue(result['verified'], f"{view} should match for Caro Test")
                    else:
                        if result['verified']:
                            print(f"⚠️ WARNING: False positive detected - {view} matched for {face['name']}")
                        self.assertFalse(result['verified'], f"{view} should not match for {face['name']}")
