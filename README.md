# vous✅ **README.md — Détection d’Émotions à partir du Visage (CNN + FastAPI + OpenCV)**

```markdown
# 🎭 Détection d’Émotions à partir du Visage  
TensorFlow • FastAPI • OpenCV • PostgreSQL • Pytest • GitHub Actions

Ce projet permet de détecter l’émotion d’un visage à partir d’une image.  
Il utilise un modèle CNN, OpenCV pour la détection de visage, une API FastAPI, une base PostgreSQL pour l’historique, ainsi qu’un pipeline de tests CI via GitHub Actions.

---

## 🚀 1. Préparation des données

Chargement :

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    image_size=(48, 48),
    batch_size=32,
    label_mode="categorical"
)
````

Prétraitement :

* Normalisation : `x/255`
* Redimensionnement : `(48, 48)`
* Data augmentation (flip, rotation, zoom)

---

## 🧠 2. Entraînement du modèle CNN

Architecture utilisée :

* Conv2D → MaxPool → Conv2D → MaxPool
* Flatten
* Dense + Dropout
* Dense softmax (7 classes d’émotion)

Compilation :

```python
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

Entraînement + sauvegarde :

```python
model.fit(train_ds, epochs=20)
model.save("emotion_detection.keras")
```

---

## 🙂 3. Détection du visage avec OpenCV

Chargement Haar Cascade :

```python
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
```

Étapes :

1. Détecter le visage
2. Extraire la ROI
3. Redimensionner en 48x48
4. Normaliser et prédire avec le CNN

Script principal : **detect_and_predict.py**

```python
def detect_and_predict(image_bytes):
    # Détecte le visage, prépare l'image et retourne l'émotion + score
```

---

## 🖥️ 4. API FastAPI

### ▶️ POST `/predict_emotion`

Reçoit un fichier image, détecte le visage et retourne :

```json
{
  "emotion": "happy",
  "score": 0.879
}
```

### ▶️ GET `/history`

Retourne l’historique des prédictions enregistrées dans PostgreSQL via SQLAlchemy.

---


---

## 🧪 5. Tests unitaires (pytest)

Tests inclus :

* Vérification que le modèle est bien chargé
* Vérification du format JSON renvoyé
* Appels API via TestClient

Lancer :

```
pytest -v
```

---

## 🔄 7. Intégration Continue (GitHub Actions)

Pipeline CI :

* Installation des dépendances
* Exécution des tests Pytest
* Vérification du modèle et des endpoints

Fichier : `.github/workflows/tests.yml`

---

## 📦 Installation

```
pip install -r requirements.txt
```

---

## ▶️ Lancer l’API

```
uvicorn main:app --reload
```

Docs Swagger :

```
http://localhost:8000/docs
```

---

## 📚 Technologies

* **TensorFlow / Keras**
* **OpenCV**
* **FastAPI**
* **SQLAlchemy + PostgreSQL**
* **Pytest**
* **GitHub Actions**

---

 
