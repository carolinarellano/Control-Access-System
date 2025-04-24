import cv2
import os
from app.db import insert_face

def capture_image(prompt, save_path):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return False

    print(prompt)
    print("Presiona 'c' para capturar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error capturando imagen.")
            break

        cv2.imshow("Captura", frame)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.imwrite(save_path, frame)
            print(f"Imagen guardada en {save_path}")
            break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return True

def register_face():
    name = input("Nombre de la persona: ").strip()

    os.makedirs("temp", exist_ok=True)
    front = "temp/front.jpg"
    right = "temp/right.jpg"
    left = "temp/left.jpg"

    if not capture_image("Mira al frente.", front):
        return
    if not capture_image("Mira hacia tu derecha (perfil izquierdo).", right):
        return
    if not capture_image("Mira hacia tu izquierda (perfil derecho).", left):
        return

    insert_face(name, front, right, left)
    print(f"Registro completado para: {name}")

if __name__ == "__main__":
    register_face()
    print("Registro de cara finalizado.")