from fastapi import FastAPI
from router.router import user
from fastapi.middleware.cors import CORSMiddleware

#uvicorn main:app --reload (Comando para iniciar el server)

app = FastAPI() #Inicio de la app
app.include_router(user) #Incluye el enrutador "user" en la aplicación principal

origins = [
    "http://localhost",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
