from fastapi import FastAPI
from pydantic import BaseModel
#from uuid import uuid4 - Libreria para utilizar datos aleatorios

app = FastAPI()

#SECCION USUARIOS

class Usuarios(BaseModel): #Clase Usuarios
    id: int 
    name_complete: str 
    direccion: str
    pais: str
    tel: int
   
usuarios = [] #Lista datos usuarios 

@app.get("/usuarios") #GET de usuarios
def get_usuarios(): 
    return usuarios

@app.get("/usuarios/{id}")# GET de usuarios con id
def get_usuarios(id: str): 
    for usuario in usuarios: 
        if usuario["id"] == id: 
            return usuario 
    return "No existe el usuario"

@app.post("/usuarios") #POST para almacenar datos de usuarios
def save_usuario(usuario: Usuarios): 
    #student.id = str(uuid4()) #El uuid4 genera un codigo al azar
    usuarios.append(usuario.dict()) 
    return "Usuario Registrado"

@app.put("/usuarios/{id}") #PUT para modificar datos de usuario ya almacenado
def update_usuario(updated_updated: Usuarios, id:str): 
    for usuario in usuarios: 
        if usuario["id"] == id:
            usuario["name"] = updated_updated.name_complete 
            usuario["direccion"] = updated_updated.direccion
            usuario["pais"] = updated_updated.pais
            usuario["tel"] = updated_updated.tel
            return "Usuario Modificado" 
    return "No existe el usuario"

@app.delete("/usuarios/{id}") #DELETE para eliminar datos de usuarios ya almacenados 
def delete_usuario(id: str): 
    for usuario in usuarios: 
        if usuario["id"] == id: 
            usuarios.remove(usuario) 
            return "Usuario Eliminado" 
    return "No existe el usuario, por favor revise los datos ingresados."

#SECCION VEHICULOS

class Vehiculos(BaseModel): #Clase Usuarios
    num_serie: int 
    marca: str 
    modelo: str
    año: int
    tipo: str
    precio: int

vehiculos = [] #Lista datos vehiculos

@app.get("/vehiculos") #GET de vehiculos
def get_vehiculos(): 
    return vehiculos

@app.get("/vehiculos/{num_serie}")# GET de vehiculos con numero de serie
def get_vehiculos(num_serie: str): 
    for vehiculo in vehiculos: 
        if vehiculos["num_serie"] == num_serie: 
            return vehiculo 
    return "No existe el vehiculo"

@app.post("/vehiculos") #POST para almacenar datos de los vehiculos
def save_vehiculo(vehiculo: Vehiculos): 
    vehiculos.append(vehiculo.dict()) 
    return "vehiculo Registrado"

@app.put("/vehiculo/{num_serie}") #PUT para modificar datos de vehiculos ya almacenados
def update_vehiculo(updated_updated: Vehiculos, num_serie:str): 
    for vehiculo in vehiculos: 
        if vehiculo["num_serie"] == num_serie:
            vehiculo["marca"] = updated_updated.marca 
            vehiculo["modelo"] = updated_updated.modelo
            vehiculo["año"] = updated_updated.año
            vehiculo["tipo"] = updated_updated.tipo
            vehiculo["precio"] = updated_updated.precio
            return "Vehiculo Modificado" 
    return "No existe el vehiculo"

@app.delete("/vehiculos/{num_serie}") #DELETE para eliminar datos de vehiculos almacenados
def delete_vehiculo(num_serie: str): 
    for vehiculo in vehiculos: 
        if vehiculo["num_serie"] == num_serie: 
            vehiculos.remove(vehiculo) 
            return "Vehiculo Eliminado" 
    return "No existe el vehiculo, por favor revise los datos ingresados."

#SECCION PEDIDOS

class Pedidos(BaseModel): #Clase Pedidos
    num_pedido: int 
    cantidad: int
    descripcion: str
    metodo_pago: str

pedidos = [] #Lista datos pedidos

@app.get("/pedidos") #GET de pedidos
def get_pedidos(): 
    return pedidos

@app.get("/pedidos/{num_pedido}")# GET de usuarios con numero de pedido
def get_pedidos(num_pedido: str): 
    for pedido in pedidos: 
        if pedido["num_pedido"] == num_pedido: 
            return pedido 
    return "No existe el pedido"

@app.post("/pedidos") #POST para almacenar datos de pedidos
def save_pedidos(pedido: Pedidos): 
    pedidos.append(pedido.dict()) 
    return "Pedido Registrado"

@app.put("/pedidos/{num_pedido}") #PUT para modificar datos de pedidos almacenados
def update_pedidos(updated_updated: Pedidos, num_pedido:str): 
    for pedido in pedidos: 
        if pedido["num_pedido"] == num_pedido:
            pedido["cantidad"] = updated_updated.cantidad 
            pedido["descripcion"] = updated_updated.descripcion
            pedido["metodo_pago"] = updated_updated.metodo_pago
            return "Pedido Modificado" 
    return "No existe el pedido"

@app.delete("/pedidos/{num_pedido}") #DELETE para eliminar datos de pedidos almacenados 
def delete_pedidos(num_pedido: str): 
    for pedido in pedidos: 
        if pedido["num_pedido"] == num_pedido: 
            pedidos.remove(pedido) 
            return "Pedido Eliminado" 
    return "No existe el pedido, por favor revise los datos ingresados."
