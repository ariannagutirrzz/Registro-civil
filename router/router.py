from fastapi import APIRouter
from schema.schemasTables import SchemaNacimientos, SchemaCiudadanos, SchemaMatrimonios, SchemaDivorcios, SchemaDefunciones
from schema.schemasUpdates import SchemaCiudadanosUpdate, SchemaMatrimoniosUpdate, SchemaNacimientosUpdate, SchemaDefuncionesUpdate, SchemaDivorciosUpdate
from config.db import UserConnection
from pdfgenerator.pdf import create_partida_nacimiento, create_acta_matrimonio, create_acta_ciudadano, create_acta_defuncion, create_acta_divorcio, create_stadistics
from datetime import date

user = APIRouter() #Crea un enrutador llamado "user"
conn = UserConnection() #Instancia de la conexion a la BDD

#NACIMIENTOS
#Ruta para insertar nacimientos
@user.post("/Nacimientos/insert")
def insertNacimientos(nacimientos: SchemaNacimientos):
    #Convierte los datos en un diccionario para mejor organizacion
    data = dict(nacimientos)
    data.pop("id")
    conn.insert_into_table('"Nacimientos"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Nacimientos
@user.get("/Nacimientos/read")
def readNacimientos():
    return conn.read('"Nacimientos"')

#Ruta para retornar los valores que hay en la tabla Nacimientos por cedula
@user.get("/Nacimientos/read/{table_id}")
def readNacimientosID(table_id: int):
    data = conn.read_by_id('"Nacimientos"', table_id)
    data = data[0]
    return data

#Ruta para generar partida de nacimiento
@user.get("/Nacimientospdf/read/{table_id}")
def readNacimientosPdf(table_id: int):
    data = conn.read_by_id('"Nacimientos"', table_id)
    data = data[0]
    create_partida_nacimiento(data)

#Ruta para eliminar algun nacimiento
@user.delete("/Nacimientos/delete/{table_id}")
def deleteNacimientos(table_id: int):
    conn.delete_id('"Nacimientos"',table_id)

#Ruta para actulizar algun dato de nacimiento
@user.put("/Nacimientos/update/{table_id}")
def updateNacimientos(table_id: int, nacimientos: SchemaNacimientosUpdate):
    conn.update_field_id('"Nacimientos"', table_id, dict(nacimientos))

#CIUDADANOS
#Ruta para insertar ciudadanos
@user.post("/Ciudadanos/insert")
def insertCiudadanos(ciudadanos: SchemaCiudadanos):
    data = dict(ciudadanos)
    conn.insert_into_table('"Ciudadanos"', data)
    print(data)


#Ruta para retornar los valores que hay en la tabla Ciudadanos por cedula
@user.get("/Ciudadanos/read/{cedula}")
def readCiudadanosID(cedula: int):
    return conn.read_by_cedula('"Ciudadanos"', cedula)

#Ruta para generar Acta de ciudadania
@user.get("/Ciudadanospdf/read/{cedula}")
def readCiudadanosPdf(cedula: int):
    data = conn.read_by_cedula('"Ciudadanos"', cedula)
    data = data[0]
    create_acta_ciudadano(data)

#Ruta para retornar los valores que hay en la tabla Ciudadanos
@user.get("/Ciudadanos/read")
def readCiudadanos():
    return conn.read_ciudadano('"Ciudadanos"', '"Nacimientos"')

#Ruta para eliminar algun ciudadano
@user.delete("/Ciudadanos/delete/{cedula}")
def deleteCiudadanos(cedula: int):
    conn.delete_cedula('"Ciudadanos"',cedula)

#Ruta para actulizar algun dato de ciudadanos
@user.put("/Ciudadanos/update/{cedula}")
def updateCiudadanos(cedula: int, ciudadanos: SchemaCiudadanosUpdate):
    data = dict(ciudadanos)
    conn.update_field_cedula('"Ciudadanos"', cedula, data)

#MATRIMONIOS
#Ruta para insertar matrimonios
@user.post("/Matrimonios/insert")
def insertMatrimonios(matrimonios: SchemaMatrimonios):
    data = dict(matrimonios)
    conn.insert_into_table('"Matrimonios"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Matrimonios
@user.get("/Matrimonios/read")
def readMatrimonios():
    return conn.read('"Matrimonios"') 

#Ruta para retornar los valores que hay en la tabla Matrimonios por id
@user.get("/Matrimonios/read/{table_id}")
def readMatrimoniosID(table_id: int):
    data = conn.read_by_id('"Matrimonios"', table_id)
    data = data[0]
    return data

#Ruta para generar acta de matrimonios
@user.get("/Matrimoniospdf/read/{table_id}")
def readMatrimoniosPdf(table_id: int):
    data = conn.read_by_id('"Matrimonios"', table_id)
    data = data[0]
    create_acta_matrimonio(data)

#Ruta para eliminar algun matrimonio
@user.delete("/Matrimonios/delete/{table_id}")
def deleteMatrimonios(table_id: int):
    conn.delete_id('"Matrimonios"',table_id)

#Ruta para actulizar algun dato de matrimonio
@user.put("/Matrimonios/update/{table_id}")
def updateMatrimonios(table_id: int, matrimnoios: SchemaMatrimoniosUpdate):
    conn.update_field_id('"Matrimonios"', table_id, dict(matrimnoios))

#DIVORCIOS
#Ruta para insertar divorcios
@user.post("/Divorcios/insert")
def insertDivorcios(divorcios: SchemaDivorcios):
    data = dict(divorcios)
    conn.insert_into_table('"Divorcios"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Divorcios
@user.get("/Divorcios/read")
def readDivorcios():
    return conn.read('"Divorcios"')

#Ruta para retornar los valores que hay en la tabla Divorcios por id
@user.get("/Divorcios/read/{table_id}")
def readDivorciosID(table_id: int):
    data = conn.read_by_id('"Divorcios"', table_id)
    data = data[0]
    return data

#Ruta para generar acta de divorcios
@user.get("/Divorciospdf/read/{table_id}")
def readDivorciosPdf(table_id: int):
    data = conn.read_by_id('"Divorcios"', table_id)
    data = data[0]
    create_acta_divorcio(data)

#Ruta para eliminar algun divorcio
@user.delete("/Divorcios/delete/{table_id}")
def deleteDivorcios(table_id: int):
    conn.delete_id('"Divorcios"',table_id)

#Ruta para actulizar algun dato de divorcio
@user.put("/Divorcios/update/{table_id}")
def updateDivorcios(table_id: int, divorcios: SchemaDivorciosUpdate):
    conn.update_field_id('"Divorcios"', table_id, dict(divorcios))

#DEFUNCIONES
#Ruta para insertar defuneciones
@user.post("/Defunciones/insert")
def insertDefunciones(defunciones: SchemaDefunciones):
    data = dict(defunciones)
    conn.insert_into_table('"Defunciones"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Defunciones
@user.get("/Defunciones/read")
def readDefunciones():
    return conn.read('"Defunciones"')

#Ruta para retornar los valores que hay en la tabla Defunciones por cedula
@user.get("/Defunciones/read/{cedula}")
def readDefuncionesID(cedula: int):
    data = conn.read_by_cedula('"Defunciones"', cedula)
    data = data[0]
    return data

#Ruta para generar acta de defunciones
@user.get("/Defuncionespdf/read/{cedula}")
def readDefuncionesPdf(cedula: int):
    data = conn.read_by_cedula('"Defunciones"', cedula)
    data = data[0]
    create_acta_defuncion(data)

#Ruta para eliminar algunas defuncion
@user.delete("/Defunciones/delete/{cedula}")
def deleteDefunciones(cedula: int):
    conn.delete_cedula('"Defunciones"',cedula)

#Ruta para actualizar alguna defuncion
@user.put("/Defunciones/update/{cedula}")
def updateDefunciones(cedula: int, defunciones: SchemaDefuncionesUpdate):
    conn.update_field_cedula('"Defunciones"', cedula, dict(defunciones))

#STATS
@user.get("/Estadisticas/read")
def readStats(date_start: date, date_end: date, lugar_nacimiento: str, parroquia: str):
    data = conn.stadistics(date_start, date_end, lugar_nacimiento, parroquia)
    create_stadistics(data, date_start, date_end, lugar_nacimiento, parroquia)
    return data