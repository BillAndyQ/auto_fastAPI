from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.products.routes import router as router_productos
from src.productos.routes import router as router_productos_2
from src.auth.auth import app as router_auth
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(router_productos, prefix="/productos")
app.include_router(router_productos_2, prefix="/productos_2")
app.include_router(router_auth)

# Configuración de orígenes permitidos
origins = [
    "http://localhost:3000",  # Tu frontend local
    "http://127.0.0.1:3000", # Alternativa si accedes desde esta dirección
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos
    allow_credentials=True, # Si manejas cookies o tokens
    allow_methods=["*"],    # Métodos HTTP permitidos (GET, POST, etc.)
    allow_headers=["*"],    # Encabezados permitidos
)

@app.get("/")
def read_root():

    return RedirectResponse(url="/docs/")