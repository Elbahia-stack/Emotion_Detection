from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from model import Prediction
from detect_and_predict import detect_and_predict  # <-- import de ta fonction

app = FastAPI(title="Emotion Detection API",debug=True)

# Crée la base si elle n’existe pas
Base.metadata.create_all(bind=engine)
@app.get("/")
def say_hello():
    return {"message": "Hello, World!"}
# Route POST /predict_emotion
@app.post("/predict_emotion")
async def predict_emotion(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()

    label, score = detect_and_predict(contents)  

    if label is None:
        raise HTTPException(status_code=400, detail="Aucun visage détecté.")

  
    new_pred = Prediction(emotion=label, score=score)
    db.add(new_pred)
    db.commit()
    db.refresh(new_pred)

    return JSONResponse({
        "emotion": label,
        "score": round(score, 3),
       
    })

@app.get('/history')
async def history(db: Session=Depends(get_db)):
    all_row=db.query(Prediction).all()
    for a in all_row:
      return[{ 'id':a.id,
              'emotion':a.emotion,
              'score':a.score}]
    