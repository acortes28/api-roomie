import dto
from pydantic import BaseModel
import entity



class RoomieService(BaseModel):
    
    def agregarRoomie(self, objRoomie : entity.Roomie):
        try:
            dto.Roomie.create(nombre=objRoomie.nombre,
                            rut=objRoomie.rut, 
                            DV=objRoomie.DV)
            return "Registro Creado exitosamente"
        except:
            return "No se pude crear el registro solicitado"
 
 
 
        
class GastosService(BaseModel):
    
    def agregarGasto(self, objGasto : entity.Gastos):
        try:
            dto.Gastos.create(idCategoria=objGasto.idCategoria,
                              descripcion=objGasto.descripcion,
                              monto=objGasto.monto,
                              fechaIncurrido=objGasto.fechaIncurrido,
                              idRoomie=objGasto.idRoomie,
                              )
            return "Gasto agregado Correctamente"
        except:
            return "No se pudo agregar el gasto solicitado"