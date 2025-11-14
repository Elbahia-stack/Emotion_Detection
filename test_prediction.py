# test_prediction.py
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from main import app
from database import get_db

# 🔹 Mock get_db pour que les tests passent sans base de données
app.dependency_overrides[get_db] = lambda: MagicMock()
client = TestClient(app)
def test_shape():
    files = {"file": ("m1.jpg", open("m1.jpg", "rb"), "image/jpeg")}
    api=client.post('/predict_emotion',files=files)
    resultat=api.json()
    
    assert isinstance(resultat, dict)
    assert isinstance(resultat["emotion"], str) 
    assert isinstance(resultat["score"], float)