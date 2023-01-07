from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from predictme import predictme
import uvicorn
import numpy as numpy
import pickle
import pandas as pd

#Create the app object

app = FastAPI()
pickle_in= open("bogo_uplift.pkl","rb")
model = pickle.load(pickle_in)

# class PredictConversion(BaseModel):
#     X_test: int
#Create index page
@app.get("/")
def index():
    return {"message": "Hello World"}
#create welcome page
@app.get("/Welcome")
def get_name():
    return {'Welcome to GroupBy Project': f'{name}'}

#Create prediction
@app.post("/predict")
def predict(data: predictme):
    data =data.dict()
    history = data['history']
    recency = data['recency']
    treatment = data['treatment']
    #print(model.predict([[offset,total_si_item_30days,print_position]]))
    prediction = model.predict([[history,recency,treatment]])
    # if (prediction[0]= True):
    #     prediction =" Client not affected by ad" 
    # else:
    #     prediction = "Client affected by ad"
    return {'prediction': prediction}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)