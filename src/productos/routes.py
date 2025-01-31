
from fastapi import APIRouter, Depends
from .models import Productos
from src.connect_db import SessionLocal
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

@router.get("/", response_model=list[Producto])
def get_productos(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    productos = db.query(Productos).all()

        # Reemplazar None por valores predeterminados si es necesario
    for producto in productos:
        if producto.precio is None:
            producto.precio = 0.0
        if producto.stock is None:
            producto.stock = 0

    return productos

