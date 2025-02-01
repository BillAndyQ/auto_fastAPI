
from sqlalchemy import Column, Integer, String, Float
from src.database import Base

class Almacenes(Base):
    __tablename__ = 'almacenes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    stock = Column(Integer)
    descripcion = Column(String)
    price = Column(Float)