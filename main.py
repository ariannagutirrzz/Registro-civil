from fastapi import FastAPI
from router.router import user

#uvicorn main:app --reload (Comando para iniciar el server)

app = FastAPI() #Inicio de la app
app.include_router(user) #Incluye el enrutador "user" en la aplicación principal