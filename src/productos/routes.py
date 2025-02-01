
from fastapi import APIRouter, Depends
from .models import Productos
from src.connect_db import SessionLocal
from .schemas import ProductosBase
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


@router.get("/", response_model=list[ProductosBase])
def get_productos(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    productos = db.query(Productos).all()
    return productos


@router.post("/", response_model=ProductosBase)
def post_productos(productos: ProductosBase, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    productos = Productos(
        name=productos.name, stock=productos.stock, descripcion=productos.descripcion, price=productos.price
        )
    db.add(productos)
    db.commit()
    db.refresh(productos)
    return productos
        