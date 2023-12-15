from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from joblib import load
from pydantic import BaseModel

import numpy as np
import pandas as pd

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

model = load('model.joblib')

@app.post("/predict")
def predict(item: Item):
    data = np.array([item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]).reshape(1, -1)
    prediction = int(model.predict(data))
    if prediction == 0:
        classe = "Setosa"
    elif prediction == 1:
        classe = "Versicolor"
    elif prediction == 2:
        classe = "Virginica"
    return {"Classe": classe}