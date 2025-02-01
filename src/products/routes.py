from fastapi import APIRouter, Depends
from .models import Producto
from src.connect_db import SessionLocal
from .models import Producto as ProductoModel
from .schemas import ProductoCreate, Producto
from sqlalchemy.orm import Session
from src.auth.auth import get_current_user
from sqlalchemy.inspection import inspect
from typing import List, Dict
router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para crear un producto
@router.post("/", response_model=Producto)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_producto = ProductoModel(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        stock=producto.stock)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Endpoint para obtener todos los productos
@router.get("/", response_model=list[Producto])
def obtener_productos(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    productos = db.query(ProductoModel).all()
       
    # Reemplazar None por valores predeterminados si es necesario
    for producto in productos:
        if producto.precio is None:
            producto.precio = 0.0
        if producto.stock is None:
            producto.stock = 0
    return productos

@router.get("/fields", response_model=List[Dict[str, str]])
def obtener_columnas(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Obtener las columnas y sus tipos del modelo
    columnas = []
    for column in inspect(ProductoModel).c:
        # Eliminar la columna 'id' si no se desea incluirla
        if column.name != 'id':
            columnas.append({
                "nombre": column.name,
                "tipo": str(column.type)
            })
    
    return columnas