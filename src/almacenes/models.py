
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Almacenes():
    __tablename__ = 'almacenes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    stock = Column(Integer)
    descripcion = Column(String)
    price = Column(Float)