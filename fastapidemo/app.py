from fastapi import FastAPI
from pydantic import BaseModel
from fastapidemo.conexion import connectdb

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    descripcion: str

@app.post("/libros/")
def crear_libro(libro: Libro):

    conexion = connectdb()
    cursor = conexion.cursor()
    consulta = "INSERT INTO libros (titulo, autor, descripcion) VALUES (%s, %s, %s)"
    valores = (libro.titulo, libro.autor, libro.descripcion)
    cursor.execute(consulta, valores)
    conexion.commit()
    conexion.close()
    return {"mensaje": "Libro creado correctamente"}

