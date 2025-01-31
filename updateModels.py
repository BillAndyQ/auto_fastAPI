import sys
import os
import importlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Agregar la carpeta src al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./test.db"  # Ruta a la base de datos SQLite local

# Crear motor de conexión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base para los modelos
Base = declarative_base()

# Función para importar todos los modelos dinámicamente desde un directorio
def import_all_models_from_directory(directory):
    # Recorremos el directorio para encontrar todos los archivos models.py
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Si encontramos un archivo models.py
            if file == "models.py":
                # Convertimos la ruta al formato de módulo de Python
                module_path = os.path.relpath(os.path.join(root, file), directory).replace(os.sep, '.').replace('.py', '')
                try:
                    # Importamos el módulo dinámicamente
                    importlib.import_module(module_path)
                    print(f"Importado: {module_path}")
                except ImportError as e:
                    print(f"Error al importar {module_path}: {e}")

# Llamada a la función, pasa el directorio raíz donde se encuentran los módulos
import_all_models_from_directory("src")

# Asegurarse de que la base de datos está creada para todos los modelos importados
Base.metadata.create_all(bind=engine)
