from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'Categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, unique=True, nullable=False)
    image_path = Column(String, unique=True, nullable=False)


class Product(Base):

    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('Categories.id'), nullable=False)
    category = relationship("Category")
    about = Column(Text, nullable=False)
    image_path = Column(String, unique=True, nullable=False)
    calories = Column(Integer)


class OrderItem(Base):
    __tablename__ = 'OrderItems'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ordered_time = Column(DateTime, nullable=False)
    last_time = Column(DateTime, nullable=False)
    phone_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    info = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    take_type = Column(String, nullable=False)
    payment_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
