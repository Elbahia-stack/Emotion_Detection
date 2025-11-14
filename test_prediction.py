from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_shape():
    files = {"file": ("m1.jpg", open("m1.jpg", "rb"), "image/jpeg")}
    api=client.post('/predict_emotion',files=files)
    resultat=api.json()
    
    assert isinstance(resultat, dict)
    assert isinstance(resultat["emotion"], str) 
    assert isinstance(resultat["score"], float)