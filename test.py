from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


engine = create_engine('sqlite:///C:/Users/mrart/DataGripProjects/kitaika/identifier.sqlite')  # Use your database URL here
Session = sessionmaker(bind=engine)
session = Session()

categories = session.query(models.Category).all()

for category in categories:
    print(f"Category ID: {category.id}, Category Name: {category.category}")

session.close()
