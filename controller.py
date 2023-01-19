from pydantic import BaseModel
from fastapi import FastAPI
import service
import entity

app = FastAPI()

@app.get('/')
def holamundo():
    return 'Wena Cabros'

@app.post('/agregarRoomie')
async def agregarRoomie(objRoomie : entity.Roomie):
    print(objRoomie)
    objService = service.RoomieService()
    return objService.agregarRoomie(objRoomie)

@app.post('/agregarGasto')
async def agregarGasto(objGastos : entity.Gastos):
    print(objGastos)
    objService = service.GastosService()
    return objService.agregarGasto(objGastos)
    
## Falta probar el metodo agregarGasto. Se debe añadir el metodo "agregarPresupuesto", "modificarPresupuesto" y "obtenerBalance"
