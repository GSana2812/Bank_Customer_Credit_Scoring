from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import gunicorn
import uvicorn
from joblib import load


app = FastAPI()
RANDOM_FOREST = load('random_forest_model.joblib')
DICT_VECTORIZER = load('dict_victorizer.joblib')

class CreditScoring(BaseModel):
    job: str
    duration: int
    poutcome: str



@app.post('/predict_credit')
async def predict_credit_scoring(data: CreditScoring):
    inference_test_example = DICT_VECTORIZER.transform(data.dict())
    y_pred_inference = RANDOM_FOREST.predict_proba(inference_test_example)[0,1]
    credit = int(y_pred_inference >= 0.5)

    return {"Probability":y_pred_inference,
            "Credit":credit}

