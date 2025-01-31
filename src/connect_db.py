from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./test.db"  # Ruta a la base de datos SQLite local

# Crear motor de conexión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Asegurarse de que la base de datos está creada
