import connection
import peewee



class Roomie(peewee.Model):
    idRoomie = peewee.PrimaryKeyField()
    nombre = peewee.CharField()
    rut = peewee.CharField()
    DV = peewee.CharField()
    
    class Meta:
        database = connection.database
        db_table = "Roomie"

class Categoria(peewee.Model):
    idCategoria = peewee.PrimaryKeyField()
    nombre = peewee.CharField()
    
    class Meta:
        database = connection.database
        db_table = "Categoria"    

class Gastos(peewee.Model):
    idGastos = peewee.PrimaryKeyField()
    idCategoria = peewee.ForeignKeyField(Categoria,to_field='idCategoria')
    descripcion = peewee.CharField()
    monto = peewee.CharField()
    fechaIncurrido = peewee.DateTimeField()
    idRoomie = peewee.ForeignKeyField(Roomie,to_field='idRoomie')
    
    class Meta:
        database = connection.database
        db_table = "Gastos"

class Presupuesto(peewee.Model):
    idGastos = peewee.PrimaryKeyField()
    idCategoria = peewee.ForeignKeyField(Categoria,to_field='idCategoria')
    descripcion = peewee.CharField()
    monto = peewee.CharField()
    fechaIncurrido = peewee.DateTimeField()
    idRoomie = peewee.ForeignKeyField(Roomie,to_field='idRoomie')
    
    class Meta:
        database = connection.database
        db_table = "Presupuesto"
   
#newRoomie = Roomie.create(nombre='Rodrigo Vaz',rut='25444888', DV='5')

# query = Roomie.select().where(Roomie.idRoomie.between(0, 3))

# for Roomie in query:
#     print(Roomie.idRoomie, Roomie.nombre)
