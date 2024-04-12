from pydantic import BaseModel
from datetime import date, time
from typing import Optional

#Schemas para actualizar los valores, sin cedulas ni ids.
class SchemaNacimientosUpdate(BaseModel):
    nombre: Optional[str] = None
    sexo: str
    fecha_nacimiento: date
    hora_nacimiento: time
    lugar_nacimiento: str
    padre1_cedula: Optional[int] = None
    padre2_cedula: Optional[int] = None
    testigo1_cedula: Optional[int] = None
    testigo2_cedula: Optional[int] = None
    parroquia: Optional[str] = None

class SchemaCiudadanosUpdate(BaseModel):
    nacionalidad: str
    estado_civil: str
    nacimientos_id: Optional[int] = None

class SchemaMatrimoniosUpdate(BaseModel):
    contrayente1_padre1_cedula: Optional[int] = None
    contrayente1_padre2_cedula: Optional[int] = None
    contrayente2_padre1_cedula: Optional[int] = None
    contrayente2_padre2_cedula: Optional[int] = None
    fecha_ActaMatrimonio: date

class SchemaDivorciosUpdate(BaseModel):
    divorciado1_cedula: Optional[int] = None
    divorciado2_cedula: Optional[int] = None
    fecha_ActaDivorcio: date

class SchemaDefuncionesUpdate(BaseModel):
    fecha_defuncion: date
    hora_defuncion: time
    lugar_defuncion: str
    destino_cadaver: str
    causa_defuncion: str