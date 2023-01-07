from fastapi import FASTAPI
import pandas as pd
import seaborn as sns
import plotly.express as px

import ssl
ssl._create_default_https_context= ssl._create_unverified_context


app = FASTAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

df = pd.read_csv('upliftfull.csv')

sns.pairplot(df)

fig= px.scatter(df, x="history", y="recency", text="Scatter")
fig.show()