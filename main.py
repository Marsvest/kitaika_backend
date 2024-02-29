from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

app = FastAPI()
engine = create_engine(
    'sqlite:///')
Session = sessionmaker(bind=engine)


@app.get("/api")
async def root():
    return {"message": "Hello World"}


@app.get("/api/getinfo")
async def getinfo():
    session = Session()
    categories = session.query(models.Category).all()
    session.close()
    return {"categories": [categories[i].category for i in range(len(categories))]}
