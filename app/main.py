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

        faces = get_faces()
        matched = False

        for face in faces:
            images = {
                "front": face.get("front_image"),
                "right": face.get("right_image"),
                "left": face.get("left_image"),
            }

            for position, blob in images.items():
                if blob:
                    temp_path = f"temp/temp_face_{face['id']}_{position}.jpg"
                    blob_to_image(blob, temp_path)

                    try:
                        result = compare_faces(live_path, temp_path)
                        if result["verified"]:
                            match_name = face["name"]
                            color = (0, 255, 0)
                            matched = True
                            break
                    except Exception as e:
                        print("Error de comparación:", e)
            if matched:
                break

        cv2.putText(frame, match_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow("Live Face Match", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
