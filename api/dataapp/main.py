from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from schemas import PredictionRequest, PredictionResponse
from tasks import process_data
from crud import get_data
from database import SessionLocal, engine
from model import TextClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pickle

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/train/")
def train( db: Session = Depends(get_db)):
    process_data.delay()
    return {"message": "Task started"}

@app.post("/predict/")
def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    model = TextClassifier.load_model('trained_models/model.pickle')
    vectorizer = TextClassifier.load_model('trained_models/vectorizer.pickle')

    tdifd = vectorizer.transform([request.text])
    result = model.predict(tdifd)


    return {"value":result[0]}

@app.get("/")
def root(db: Session = Depends(get_db)):
    return get_data(db)