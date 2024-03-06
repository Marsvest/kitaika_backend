from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

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


class OrderItems(Base):
    __tablename__ = 'OrderItems'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    single_price = Column(Integer, nullable=False)


class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ordered_time = Column(String, nullable=False)
    last_time = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    info = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    take_type = Column(String, nullable=False)
    payment_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    confirmed = Column(Boolean, nullable=False)
    total_price = Column(Integer, nullable=False)


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)


class OrderInit(BaseModel):
    pass


class OrderCreate(BaseModel):
    last_time: str
    phone_number: str
    name: str
    info: str
    address: str
    take_type: str
    payment_type: str


class OrderUpdate(BaseModel):
    last_time: str
    phone_number: str
    name: str
    info: str
    address: str
    take_type: str
    payment_type: str


class OrderItemsUpdate(BaseModel):
    order_id: int
    product_id: int
    count: int


class ProductCreate(BaseModel):
    label: str
    price: int
    category_id: int
    about: str
    image_path: str
    calories: int
