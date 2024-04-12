from fastapi import APIRouter
from fpdf import FPDF
from schema.schemasTables import SchemaNacimientos, SchemaCiudadanos, SchemaTestigos, SchemaMatrimonios, SchemaDivorcios, SchemaDefunciones
from config.db import UserConnection

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

#Ruta para eliminar algun nacimiento
@user.delete("/Nacimientos/delete/{cedula}")
def deleteNacimientos(table_cedula: int):
    conn.delete_cedula('"Nacimientos"',table_cedula)

#Ruta para actulizar algun dato de nacimiento
@user.put("/Nacimientos/update/{cedula}")
def updateNacimientos(cedula: int, nacimientos: SchemaNacimientos):
    conn.update_field_cedula('"Nacimientos"', cedula, dict(nacimientos))

#CIUDADANOS
#Ruta para insertar ciudadanos
@user.post("/Ciudadanos/insert")
def insertCiudadanos(ciudadanos: SchemaCiudadanos):
    data = dict(ciudadanos)
    conn.insert_into_table('"Ciudadanos"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Ciudadanos
@user.get("/Ciudadanos/read")
def readCiudadanos():
    return conn.read('"Ciudadanos"')

#Ruta para eliminar algun ciudadano
@user.delete("/Ciudadanos/delete/{cedula}")
def deleteCiudadanos(cedula: int):
    conn.delete_cedula('"Ciudadanos"',cedula)

#Ruta para actulizar algun dato de ciudadanos
@user.put("/Ciudadanos/update/{cedula}")
def updateCiudadanos(cedula: int, ciudadanos: SchemaCiudadanos):
    conn.update_field_cedula('"Ciudadanos"', cedula, dict(ciudadanos))

def create_PDF(ciudadanos: SchemaCiudadanos):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, f'Cédula: {ciudadanos.cedula}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'Nacionalidad: {ciudadanos.nacionalidad}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'Estado Civil: {ciudadanos.estado_civil}')
    pdf.ln(10)  # Nueva línea
    pdf.cell(40, 10, f'ID de Nacimiento: {ciudadanos.nacimientos_id}')
    return pdf.output(dest='S').encode('latin1')

@user.get("/Ciudadanos/read/{cedula}")
def readCiudadanosPdf(cedula):
    return conn.read_by_cedula('"Ciudadanos"', cedula)

#TESTIGOS
#Ruta para insertar testigos
@user.post("/Testigos/insert")
def insertTestigos(testigos: SchemaTestigos):
    data = dict(testigos)
    conn.insert_into_table('"Testigos"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Testigos
@user.get("/Testigos/read")
def readTestigos():
    return conn.read('"Testigos"')   

#Ruta para eliminar algun testigo
@user.delete("/Testigos/delete/{cedula}")
def deleteTestigos(table_cedula: int):
    conn.delete_cedula('"Testigos"',table_cedula)

#Ruta para actulizar algun dato de testigos
@user.put("/Testigos/update/{cedula}")
def updateTestigos(cedula: int, testigos: SchemaTestigos):
    conn.update_field_id('"Testigos"', cedula, dict(testigos))

#MATRIMONIOS
#Ruta para insertar matrimonios
@user.post("/Matrimonios/insert")
def insertMatrimonios(matrimonios: SchemaMatrimonios):
    data = dict(matrimonios)
    data.pop("id")
    conn.insert_into_table('"Matrimonios"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Matrimonios
@user.get("/Matrimonios/read")
def readMatrimonios():
    return conn.read('"Matrimonios"') 

#Ruta para eliminar algun matrimonio
@user.delete("/Matrimonios/delete/{id}")
def deleteMatrimonios(id: int):
    conn.delete_id('"Matrimonios"',id)

#Ruta para actulizar algun dato de matrimonio
@user.put("/Matrimonios/update/{id}")
def updateMatrimonios(id: int, matrimnoios: SchemaMatrimonios):
    conn.update_field_id('"Matrimonios"', id, dict(matrimnoios))

#DIVORCIOS
#Ruta para insertar divorcios
@user.post("/Divorcios/insert")
def insertDivorcios(divorcios: SchemaDivorcios):
    data = dict(divorcios)
    data.pop("id")
    conn.insert_into_table('"Divorcios"', data)
    print(data)

#Ruta para retornar los valores que hay en la tabla Divorcios
@user.get("/Divorcios/read")
def readDivorcios():
    return conn.read('"Divorcios"')

#Ruta para eliminar algun divorcio
@user.delete("/Divorcios/delete/{id}")
def deleteDivorcios(id: int):
    conn.delete_id('"Divorcios"',id)

#Ruta para actulizar algun dato de divorcio
@user.put("/Divorcios/update/{id}")
def updateDivorcios(id: int, divorcios: SchemaDivorcios):
    conn.update_field_id('"Divorcios"', id, dict(divorcios))

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

#Ruta para eliminar algun testigo
@user.delete("/Defunciones/delete/{cedula}")
def deleteDefunciones(cedula: int):
    conn.delete_cedula('"Defunciones"',cedula)

@user.put("/Defunciones/update/{cedula}")
def updateDefunciones(cedula: int, defunciones: SchemaDefunciones):
    conn.update_field_cedula('"Defunciones"', cedula, dict(defunciones))
    