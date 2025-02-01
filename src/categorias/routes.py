
from fastapi import APIRouter, Depends
from .models import Categorias
from src.connect_db import SessionLocal
from .schemas import CategoriasBase
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


@router.get("/", response_model=list[CategoriasBase])
def get_categorias(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    categorias = db.query(Categorias).all()
    return categorias


@router.post("/", response_model=CategoriasBase)
def post_categorias(categorias: CategoriasBase, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    categorias = Categorias(
        name=categorias.name
        )
    db.add(categorias)
    db.commit()
    db.refresh(categorias)
    return categorias
        