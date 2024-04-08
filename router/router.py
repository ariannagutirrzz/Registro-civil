from fastapi import APIRouter
from schema.schemasTables import SchemaNacimientos, SchemaCiudadanos, SchemaTestigos, SchemaParroquias, SchemaMatrimonios, SchemaDivorcios, SchemaDefunciones
from config.db import UserConnection

user = APIRouter() #Crea un enrutador llamado "user"
conn = UserConnection() #Instancia de la conexion a la BDD

#Ruta base o default
@user.get("/")
def root():
    return "aridna boba"

#Ruta para insertar nacimientos
@user.post("/Nacimientos/insert")
def insertNacimientos(nacimientos: SchemaNacimientos):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in nacimientos:
        data[field] = value
    conn.insert_into_table('"Nacimientos"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Nacimientos
@user.get("/Nacimientos/read")
def readNacimientos():
    return conn.read('"Nacimientos"')

#Ruta para insertar ciudadanos
@user.post("/Ciudadanos/insert")
def insertCiudadanos(ciudadanos: SchemaCiudadanos):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in ciudadanos:
        data[field] = value
    conn.insert_into_table('"Ciudadanos"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Ciudadanos
@user.get("/Ciudadanos/read")
def readCiudadanos():
    return conn.read('"Ciudadanos"')   

#Ruta para insertar testigos
@user.post("/Testigos/insert")
def insertTestigos(testigos: SchemaTestigos):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in testigos:
        data[field] = value
    conn.insert_into_table('"Testigos"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Testigos
@user.get("/Testigos/read")
def readTestigos():
    return conn.read('"Testigos"')   

#Ruta para insertar parroquias
@user.post("/Parroquias/insert")
def insertParroquias(parroquias: SchemaParroquias):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in parroquias:
        data[field] = value
    data.pop("id")
    conn.insert_into_table('"Parroquias"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Parroquias
@user.get("/Parroquias/read")
def readParroquias():
    return conn.read('"Parroquias"') 

#Ruta para insertar matrimonios
@user.post("/Matrimonios/insert")
def insertMatrimonios(matrimonios: SchemaMatrimonios):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in matrimonios:
        data[field] = value
    data.pop("id")
    conn.insert_into_table('"Matrimonios"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Parroquias
@user.get("/Matrimonios/read")
def readMatrimonios():
    return conn.read('"Matrimonios"') 

#Ruta para insertar divorcios
@user.post("/Divorcios/insert")
def insertDivorcios(divorcios: SchemaDivorcios):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in divorcios:
        data[field] = value
    data.pop("id")
    conn.insert_into_table('"Divorcios"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Divorcios
@user.get("/Divorcios/read")
def readDivorcios():
    return conn.read('"Divorcios"') 

#Ruta para insertar defuneciones
@user.post("/Defunciones/insert")
def insertDefunciones(defunciones: SchemaDefunciones):
    data = {}
    #Convierte los datos en un diccionario para mejor organizacion
    for field, value in defunciones:
        data[field] = value
    conn.insert_into_table('"Defunciones"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Defunciones
@user.get("/Defunciones/read")
def readDefunciones():
    return conn.read('"Defunciones"') 