
from pydantic import BaseModel
from typing import List

class ProductosBase(BaseModel):

    name: str
    stock: int
    descripcion: str
    price: float
    categoria_id: int