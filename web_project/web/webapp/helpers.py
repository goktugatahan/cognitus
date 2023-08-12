import os
import requests
from urllib import parse

AI_API_URL = os.getenv("AI_API_URL")

def train():
    resp = requests.post(
        parse.urljoin(AI_API_URL,"train")
    )
    return resp.json()

def predict(text:str):
    resp = requests.post(
        parse.urljoin(AI_API_URL,"predict"),
        json={"text":text}
    )
    return resp.json()
