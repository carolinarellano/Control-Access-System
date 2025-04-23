import unittest
from app.db import insert_face, get_faces

class TestDB(unittest.TestCase):
    def test_insert_and_fetch(self):
        insert_face("Test", "face_database/caro.jpg")
        faces = get_faces()
        self.assertTrue(any(f['name'] == "Test" for f in faces))