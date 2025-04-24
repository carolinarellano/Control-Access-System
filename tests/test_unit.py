import unittest
from app.db import insert_face, get_faces

class TestFaceRegistration(unittest.TestCase):
    def test_insert_and_fetch_face(self):
        insert_face("Caro Test", 
                    "face_database/front.jpg", 
                    "face_database/right.jpg", 
                    "face_database/left.jpg")

        faces = get_faces()

        match = next((f for f in faces if f['name'] == "Caro Test"), None)

        # Verificar que fue insertada correctamente
        self.assertIsNotNone(match)
        self.assertIsNotNone(match['front_image'])
        self.assertIsNotNone(match['right_image'])
        self.assertIsNotNone(match['left_image'])

if __name__ == "__main__":
    unittest.main()
