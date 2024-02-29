from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

app = FastAPI()
engine = create_engine(
    'sqlite:///kitaika.db')
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/api")
async def root():
    return {"api_documentation": "https://github.com/Marsvest/kitaika_backend/blob/master/README.md"}


def get_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories


@app.get("/api/getcategories")
async def get_categories_route(categories: list = Depends(get_categories)):
    return {
        "categories": [{"name": category.category, "image_path": category.image_path} for category in categories]
    }


@app.get("/api/getproducts")
async def getproducts(category_id: int):
    return
