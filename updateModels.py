import sys
import os
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Agregar la carpeta src al PYTHONPATH
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)
print(f"Agregado al PYTHONPATH: {src_path}")

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./test.db"  # Ruta a la base de datos SQLite local
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Importar Base desde el módulo común
from src.database import Base

# Función para importar todos los modelos dinámicamente desde un directorio
def import_all_models_from_directory(directory):
    print(f"Buscando modelos en: {directory}")
    for root, dirs, files in os.walk(directory):
        print(f"Explorando: {root}")
        for file in files:
            if file == "models.py":
                rel_path = os.path.relpath(os.path.join(root, file), directory)
                module_path = rel_path.replace(os.sep, '.').replace('.py', '')
                print(f"Intentando importar: {module_path}")
                try:
                    module = importlib.import_module(module_path)
                    print(f"Importado: {module_path}")
                    # Verifica que los modelos estén en el módulo
                    for name, obj in module.__dict__.items():
                        if isinstance(obj, type) and issubclass(obj, Base) and obj != Base:
                            print(f"Modelo encontrado: {name}")
                except ImportError as e:
                    print(f"Error al importar {module_path}: {e}")
                except Exception as e:
                    print(f"Error inesperado al importar {module_path}: {e}")

# Llamada a la función, pasa el directorio raíz donde se encuentran los módulos
import_all_models_from_directory("src")

# Asegurarse de que la base de datos está creada para todos los modelos importados
print("Creando tablas...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas.")