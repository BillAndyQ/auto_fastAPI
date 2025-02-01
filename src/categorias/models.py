
from sqlalchemy import Column, Integer, String, Float
from src.database import Base
from sqlalchemy.orm import relationship


class Categorias(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    productos = relationship("Productos", back_populates="categoria")