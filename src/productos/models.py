
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.database import Base
from sqlalchemy.orm import relationship

class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    stock = Column(Integer)
    descripcion = Column(String)
    price = Column(Float)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

    categoria = relationship("Categorias", back_populates="productos")