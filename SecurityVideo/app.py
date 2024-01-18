import cv2
import os
import time
from flask import Flask, render_template, Response

app = Flask(__name__)

# Configuración de la cámara
camera = cv2.VideoCapture(0) #
camera.set(3, 640)  # Ancho del frame
camera.set(4, 480)  # Altura del frame
# Directorio para almacenar imágenes capturadas
storage_directory = 'captured_images'

if not os.path.exists(storage_directory):
    os.mkdir(storage_directory)

# Función para la detección de movimiento usando Diferencia de Fotogramas
def detect_motion(frame1, frame2):
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame_diff = cv2.absdiff(frame1_gray, frame2_gray)
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    motion_detected = any(cv2.contourArea(cnt) > 500 for cnt in contours)
    return motion_detected

# Función para capturar imágenes y detectar movimiento
def capture_and_detect_motion():
    prev_frame = None

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        if prev_frame is not None:
            motion_detected = detect_motion(prev_frame, frame)

            # Si se detecta movimiento, guarda la imagen en el directorio de almacenamiento
            if motion_detected:
                timestamp = time.strftime('%Y%m%d%H%M%S')
                image_path = os.path.join(storage_directory, f'image_{timestamp}.jpg')
                cv2.imwrite(image_path, frame)

        prev_frame = frame

        # Codificar el frame como imagen JPEG para mostrarlo en el navegador web
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Ruta para la transmisión en vivo en el navegador web
@app.route('/')
def index():
    return render_template('index.html')

# Función para transmitir el video en vivo al navegador
@app.route('/video_feed')
def video_feed():
    return Response(capture_and_detect_motion(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
