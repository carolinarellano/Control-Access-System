# Control-Access-System
## IOT Project
### Description
This project is a Control Access System that uses a PicoImx8M Plus board to control access to a door. The system uses a camera to capture images of people trying to access the door and uses a machine learning model to determine if the person is authorized to enter, also uses a RFID card to. The system also includes a web interface for monitoring and controlling access.

### Features
- Real-time image capture and processing
- Machine learning model for face recognition
- RFID card reader for access control
- Web interface for monitoring and controlling access
- User management system for adding and removing authorized users

## Setup
1. Create a DynamoDB database and table:

```sql
CREATE TABLE face_database (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    front_image LONGBLOB,
    right_image LONGBLOB,
    left_image LONGBLOB
);
```
2. Update `db.py` with your database credentials.
3. Install dependencies:
```bash
pip install -r requirements.txt
```
```bash
$env:PYTHONPATH="."
```

## Run the app
```bash
python run.py
```

## Run tests
```bash
pytest tests/
```