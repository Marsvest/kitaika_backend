from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from datetime import datetime

engine = create_engine('sqlite:///kitaika.db')  # Use your database URL here
Session = sessionmaker(bind=engine)
session = Session()

categories = session.query(models.Orders).all()

for category in categories:
    print(category.ordered_time)
    print(datetime.fromtimestamp(category.ordered_time/1000))

session.close()
