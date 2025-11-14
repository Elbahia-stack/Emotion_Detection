import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

model = load_model('emotion_detection.keras')

# Charger le classifieur Haar Cascade pour détecter les visages
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class_names = ['angry', 'happy', 'sad', 'surprised', 'neutral']
img = cv2.imread('m1.jpg')



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,               # image en niveaux de gris
    scaleFactor=1.1,    # paramètre de réduction d’échelle
    minNeighbors=5,     # combien de voisins pour valider une détection
    minSize=(40, 40)    # taille minimale du visage détecté
)

#  Pour chaque visage détecté, on effectue la prédiction
for (x, y, w, h) in faces:
    # Extraire la région du visage
    face = img[y:y+h, x:x+w]

    # Redimensionner selon la taille attendue par le model
    face_resized = cv2.resize(face, (48, 48))

    # Normaliser les pixels 
    face_normalized = face_resized / 255.0

    # Ajouter une dimension pour le batch (1, 128, 128, 3)
    face_input = np.expand_dims(face_normalized, axis=0)

    # Prédiction avec le modèle
    prediction = model.predict(face_input)
    predicted_class = np.argmax(prediction)
 
    label = class_names[predicted_class]

    # Afficher le rectangle et le label sur l’image
    cv2.rectangle(img, (x, y), (x+w, y+h), (203, 195, 255), 3)
    cv2.putText(img, label, (x+60, y-30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                2, (203, 195, 255), 3, cv2.LINE_AA)
    
#Afficher le résultat
cv2.imshow('Résultat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()