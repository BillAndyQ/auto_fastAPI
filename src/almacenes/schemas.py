
from pydantic import BaseModel
from typing import List

class AlmacenesBase(BaseModel):

    name: str
    stock: int
    descripcion: str
    price: float