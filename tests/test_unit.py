import unittest
import os
from unittest.mock import patch, MagicMock
from app import db, camera, storage, compare
from deepface import DeepFace

class TestDatabase(unittest.TestCase):
    @patch('app.db.mysql.connector.connect')
    def test_connect_db(self, mock_connect):
        mock_connect.return_value = MagicMock()
        conn = db.connect_db()
        self.assertIsNotNone(conn)

    def test_insert_face_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            db.insert_face("Test", "invalid.jpg", "invalid.jpg", "invalid.jpg")

    def test_get_faces(self):
        faces = db.get_faces()
        self.assertIsInstance(faces, list)

class TestCamera(unittest.TestCase):
    def test_capture_frame_creates_file(self):
        path = "temp/test_frame.jpg"
        camera.capture_frame(path)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

class TestStorage(unittest.TestCase):
    def test_blob_to_image_creates_image(self):
        with open("face_database/sample.jpg", "rb") as f:
            blob = f.read()
        path = "temp/blob_image.jpg"
        storage.blob_to_image(blob, path)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

class TestCompare(unittest.TestCase):
    def test_compare_faces_output(self):
        result = compare.compare_faces("face_database/caro.jpg", "face_database/caro.jpg")
        self.assertIn('verified', result)

class TestFaceRegistration(unittest.TestCase):
    def test_register_face_success(self):
        db.insert_face("Unit Test", "face_database/caro.jpg", "face_database/caro.jpg", "face_database/caro.jpg")
        faces = db.get_faces()
        self.assertTrue(any(face['name'] == "Unit Test" for face in faces))

if __name__ == '__main__':
    unittest.main()
