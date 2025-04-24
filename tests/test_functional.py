import unittest
import os
from app.db import get_faces, insert_face
from app.storage import blob_to_image
from deepface import DeepFace

class TestFunctional(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.name = "Caro Funcional"
        cls.front_path = "face_database/func_front.jpg"
        cls.right_path = "face_database/func_right.jpg"
        cls.left_path = "face_database/func_left.jpg"
        insert_face(cls.name, cls.front_path, cls.right_path, cls.left_path)

    def test_registration_saves_three_images(self):
        faces = get_faces()
        target = next((f for f in faces if f["name"] == self.name), None)
        self.assertIsNotNone(target)
        self.assertTrue(target["front_image"])
        self.assertTrue(target["right_image"])
        self.assertTrue(target["left_image"])

    def test_face_verification_match(self):
        faces = get_faces()
        target = next((f for f in faces if f["name"] == self.name), None)
        for view in ["front_image", "right_image", "left_image"]:
            temp_path = f"temp/test_match_{view}.jpg"
            blob_to_image(target[view], temp_path)
            result = DeepFace.verify(self.front_path, temp_path, enforce_detection=False)
            os.remove(temp_path)
            self.assertTrue(result["verified"], f"{view} should match")

    def test_face_verification_no_match(self):
        faces = get_faces()
        target = next((f for f in faces if f["name"] != self.name), None)
        if target:
            for view in ["front_image", "right_image", "left_image"]:
                if target[view]:
                    temp_path = f"temp/test_nomatch_{view}.jpg"
                    blob_to_image(target[view], temp_path)
                    result = DeepFace.verify(self.front_path, temp_path, enforce_detection=False)
                    os.remove(temp_path)
                    self.assertFalse(result["verified"], f"{view} should not match")

if __name__ == "__main__":
    unittest.main()
