from fastapi import FastAPI
from pydantic import BaseModel
from conexion import connectdb

app = FastAPI()

class Libro(BaseModel):
    nombre_libro: str
    autor_libro: str
    editorial_libro: str

@app.get("/")
def root():
    return {"mensaje": "Hola mundo"}

@app.post("/libros/")
def crear_libro(libro: Libro):

    conexion = connectdb()
    if not conexion:
        return {"mensaje": "Error al conectar a la base de datos"}

    cursor = conexion.cursor()
    try:
        query = f"INSERT INTO libro (nombre_libro, autor_libro, editorial_libro) VALUES ('{libro.nombre_libro}', " \
                f"'{libro.autor_libro}', '{libro.editorial_libro}')"

        cursor.execute(query)
        id_libro = cursor.lastrowid
        conexion.commit()
        nombre_libro = libro.nombre_libro
        conexion.close()
        return f"Libro {nombre_libro} insertado correctamente con id {id_libro}"

    except Exception as e:
        print("Ocurrió un error al insertar, detalle del error: ", e)
        return {"mensaje": "Error al insertar el libro"}

#obtener los libros llave valor en formato json
@app.get("/get_libros/")
def obtener_libros():
    conexion = connectdb()
    if not conexion:
        return {"mensaje": "Error al conectar a la base de datos"}

    cursor = conexion.cursor()
    try:
        query = f"SELECT * FROM libro"
        cursor.execute(query)
        libros = cursor.fetchall()
        data = []
        for libro in libros:
            item ={}
            for i in range(len(libro)):
                item[cursor.description[i][0]] = libro[i]
            data.append(item)
                # obtener las versiones de los libros
            query = f"SELECT * FROM versiones WHERE id_libro = {libro[0]}"
            cursor.execute(query)
            versiones = cursor.fetchall()
            item["versiones"] = []
            for version in versiones:
                item_version = {}
                for i in range(len(version)):
                    item_version[cursor.description[i][0]] = version[i]
                item["versiones"].append(item_version)
        conexion.close()
        return {"libros": data}

    except Exception as e:
        print("Ocurrió un error al obtener los libros, detalle del error: ", e)
        return {"mensaje": "Error al obtener los libros"}
