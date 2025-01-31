# schemas.py
from pydantic import BaseModel

# Esquema para crear un producto
class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str = ""
    precio: float 
    stock: int = 0

# Esquema para respuesta de producto
class Producto(ProductoCreate):
    id: int

    class Config:
        orm_mode = True
