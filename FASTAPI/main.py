from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API 196",
    description="AlvarezRamirez Emilio Alejandro",
    version="1.0.1"
)

usuarios = [
    {"id": 1, "nombre": "Emilio", "edad": 37},
    {"id": 2, "nombre": "Zoe", "edad": 22},
    {"id": 3, "nombre": "Tiamat", "edad": 21},
    {"id": 4, "nombre": "Yeriel", "edad": 18},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"HOLA FastAPI": "EmiAlex"}

# Endpoint para consultar todos los usuarios
@app.get("/usuarios", tags=["Operacion CRUD"])
def consultar_todos():
    return {"Usuarios registrados": usuarios}

# Endpoint para agregar un usuario
@app.post("/usuarios/", tags=["Operacion CRUD"])
def agregar_usuario(usuarionuevo: dict):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.get("id"):
            raise HTTPException(status_code=400, detail="El id ya está registrado")
    
    usuarios.append(usuarionuevo)
    return usuarionuevo

# Endpoint para actualizar un usuario
@app.put("/usuarios/{id}", tags=["Operacion CRUD"])
def actualizar_usuario(id: int, usuario_actualizado: dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario_actualizado)
            return {"mensaje": "Usuario actualizado correctamente", "usuario": usr}
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint para eliminar un usuario
@app.delete("/usuarios/{id}", tags=["Operacion CRUD"])
def eliminar_usuario(id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(i)
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
