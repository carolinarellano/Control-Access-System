import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def insert_face(name, frontimg_path, rightimg_path, leftimg_path):
    with open(frontimg_path, 'rb') as f1, open(rightimg_path, 'rb') as f2, open(leftimg_path, 'rb') as f3:
        binary1 = f1.read()
        binary2 = f2.read()
        binary3 = f3.read()

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO face_database (name, front_image, right_image, left_image)
        VALUES (%s, %s, %s, %s)
    """, (name, binary1, binary2, binary3))
    db.commit()
    cursor.close()
    db.close()

def get_faces():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, front_image, right_image, left_image FROM face_database")
    faces = cursor.fetchall()
    cursor.close()
    db.close()
    return faces