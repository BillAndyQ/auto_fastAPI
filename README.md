## Generación automática de routes, models, schemas en FastAPI

1. Definir la estructura de las tablas en structure.json

2. Ejecuta auto_structure.ipynb

3. Ejecuta la migración de las tablas
    ```bash
    py updateModels.py

4. Instala las dependencias
    ```bash
    pip install -r requirements.txt

5. Instala las dependencias
    ```bash
    uvicorn main:app --reload