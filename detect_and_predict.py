import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Charger le modèle et le cascade Haar
model = load_model('emotion_detection.keras')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class_names = ['angry', 'disgusted','fearful','happy','neutral', 'sad', 'surprised']

# Convertir bytes en image OpenCV
def bytes_to_image(contents):
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

# Détection et prédiction pour tous les visages
def detect_and_predict(contents):
    img = bytes_to_image(contents)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )


    if len(faces) == 0:
        return None, None, img 

    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (48, 48))
        face_normalized = face_resized / 255.0
        face_input = np.expand_dims(face_normalized, axis=0)

        prediction = model.predict(face_input)
        predicted_class = np.argmax(prediction)
        score = float(np.max(prediction))
        emotion = class_names[predicted_class]

        cv2.rectangle(img, (x, y), (x+w, y+h), (203, 195, 255), 3)
        cv2.putText(img, emotion, (x, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1, (203, 195, 255), 2, cv2.LINE_AA)

        

    return emotion,score
