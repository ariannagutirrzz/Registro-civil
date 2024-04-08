from fastapi import FastAPI
from router.router import user

app = FastAPI() #Inicio de la app
app.include_router(user) #Incluye el enrutador "user" en la aplicación principal



