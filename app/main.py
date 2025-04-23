import cv2
import os
from app.db import get_faces
from app.camera import capture_frame
from app.storage import blob_to_image
from app.compare import compare_faces

def run_app():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        live_path = "temp/temp_frame.jpg"
        cv2.imwrite(live_path, frame)

        match_name = "Unknown"
        color = (0, 0, 255)

        for face in get_faces():
            path = f"temp/temp_face_{face['id']}.jpg"
            blob_to_image(face['image'], path)

            try:
                result = compare_faces(live_path, path)
                if result['verified']:
                    match_name = face['name']
                    color = (0, 255, 0)
                    break
            except Exception as e:
                print("Comparison error:", e)

        cv2.putText(frame, match_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow("Live Face Match", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()