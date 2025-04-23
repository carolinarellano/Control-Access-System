import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Andromeda11,",
        database="face_recognition"
    )

def insert_face(name, image_path):
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO face_database (name, image) VALUES (%s, %s)", (name, binary_data))
    db.commit()
    cursor.close()
    db.close()

def get_faces():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, image FROM face_database")
    faces = cursor.fetchall()
    cursor.close()
    db.close()
    return faces