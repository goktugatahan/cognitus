from celery import Celery
from crud import get_data
from model import TextClassifier
from database import SessionLocal
from sklearn.model_selection import train_test_split
import os

REDIS_HOST= os.getenv("REDIS_HOST")
REDIS_PORT= os.getenv("REDIS_PORT")

app = Celery('worker', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}/0',backend=f'redis://{REDIS_HOST}:{REDIS_PORT}/1')

@app.task()
def process_data():
    db = SessionLocal()
    text, label = get_data(db=db)

    training, vectorizer = TextClassifier.tfidf(text)
    x_train, x_test, y_train, y_test = train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = TextClassifier.test_SVM(x_train, x_test, y_train, y_test)
    TextClassifier.dump_model(model, 'trained_models/model.pickle')
    TextClassifier.dump_model(vectorizer, 'trained_models/vectorizer.pickle')