from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Data
from typing import Tuple
import pandas as pd


def get_data(db: Session) -> Tuple[list,list]:
    allDataQueryStatement = db.query(Data).statement
    df = pd.read_sql_query(allDataQueryStatement,engine)
    print(df)
    return df['text'].tolist(), df['label'].tolist()