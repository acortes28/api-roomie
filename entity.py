from pydantic import BaseModel
import datetime
from typing import Optional

class Roomie(BaseModel):
    nombre : str
    rut : int
    DV : str

class Gastos(BaseModel):
    idCategoria : int
    descripcion : str
    monto : int
    fechaIncurrido : datetime.datetime
    idRoomie : int
    
class Presupuesto(BaseModel):
    idCategoria : int
    descripcion : str
    monto : int
    fechaIncurrido : datetime.datetime
    idRoomie : int