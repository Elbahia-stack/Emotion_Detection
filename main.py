from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datetime import datetime
from database import Base, engine, get_db
from model import Prediction
from detect_and_predict import detect_and_predict  # <-- import de ta fonction

app = FastAPI(title="Emotion Detection API")

# Crée la base si elle n’existe pas
Base.metadata.create_all(bind=engine)

# Route POST /predict_emotion
@app.post("/predict_emotion")
async def predict_emotion(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()

    emotion, score = detect_and_predict(contents)
    if emotion is None:
        raise HTTPException(status_code=400, detail="Aucun visage détecté.")

    new_pred = Prediction(emotion=emotion, score=score, created_at=datetime.utcnow())
    db.add(new_pred)
    db.commit()
    db.refresh(new_pred)

    return JSONResponse({
        "emotion": emotion,
        "score": round(score, 3),
        "timestamp": new_pred.created_at
    })
