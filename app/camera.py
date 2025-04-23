import cv2

def capture_frame(save_path="temp/temp_frame.jpg"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        cv2.imwrite(save_path, frame)
        return save_path
    else:
        raise Exception("Failed to capture frame from webcam.")