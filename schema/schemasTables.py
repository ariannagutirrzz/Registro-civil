from pydantic import BaseModel
from datetime import date, time
from typing import Optional

#Modelo de datos que va a recibir la tabla nacimientos
class SchemaNacimientos(BaseModel):
    cedula: int
    nombre: str
    sexo: str
    fecha_nacimiento: date
    lugar_nacimiento: str
    padre1_cedula: Optional[int] = None
    padre2_cedula: Optional[int] = None
    testigo1_cedula: Optional[int] = None
    testigo2_cedula: Optional[int] = None
    parroquia_id: Optional[int] = None

class SchemaCiudadanos(BaseModel):
    cedula: int
    nacionalidad: str
    estado_civil: str

class SchemaTestigos(BaseModel):
    cedula: int

class SchemaParroquias(BaseModel):
    id: Optional[int] = None
    nombre: str
    estado: str
    municipio: str    

class SchemaMatrimonios(BaseModel):
    id: Optional[int] = None
    contrayente1_cedula: Optional[int] = None
    contrayente2_cedula: Optional[int] = None
    contrayente1_padre1_cedula: Optional[int] = None
    contrayente1_padre2_cedula: Optional[int] = None
    contrayente2_padre1_cedula: Optional[int] = None
    contrayente2_padre2_cedula: Optional[int] = None
    fecha_actamatrimonio: date #En la BDD sale como fecha_ActaMatrimonio, editenla y pongan todo minusculas

class SchemaDivorcios(BaseModel):
    id: Optional[int] = None
    divorciado1_cedula: Optional[int] = None
    divorciado2_cedula: Optional[int] = None
    fecha_actadivorcio: date #En la BDD sale como fecha_ActaDivorcio, editenla y pongan todo minusculas

class SchemaDefunciones(BaseModel):
    cedula: int
    fecha_defuncion: date
    hora_defuncion: time
    lugar_defuncion: str
    destino_cadaver: str
    causa_defuncion: str