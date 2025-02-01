# models.py
from sqlalchemy import Column, Integer, String, Float
from src.database import Base


class Producto(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)
    stock = Column(Integer, default=0)
