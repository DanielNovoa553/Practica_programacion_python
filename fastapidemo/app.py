from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from conexion import connectdb

app = FastAPI()

class Libro(BaseModel):
    """ Modelo para crear un libro

        Args:
                nombre_libro (str): Nombre del libro
                autor_libro (str): Autor del libro
                editorial_libro (str): Editorial del libro
    """
    nombre_libro: str
    autor_libro: str
    editorial_libro: str

@app.get("/")
def root():
    """
    Función para probar el funcionamiento de la API
    Returns:
        message (str): Mensaje de prueba

    """
    return {"mensaje": "Hola mundo"}

@app.post("/libros/", status_code=status.HTTP_201_CREATED)
def crear_libro(libro: Libro):
    """
    Función para crear un libro
    Args:
        libro ():{nombre_libro, autor_libro, editorial_libro}

    Returns:
        message (str): Mensaje de confirmación de creación del libro

    exepction:
        message (str): Mensaje de error al crear el libro
    """
    code = False
    conexion = connectdb()
    cursor = conexion.cursor()
    try:

        query = f"INSERT INTO libro (nombre_libro, autor_libro, editorial_libro) VALUES ('{libro.nombre_libro}', " \
                f"'{libro.autor_libro}', '{libro.editorial_libro}')"
        print(query)
        cursor.execute(query)
        id_libro = cursor.lastrowid
        conexion.commit()
        nombre_libro = libro.nombre_libro
        code = True
        conexion.close()
        return {
            "mensaje": f"Libro {nombre_libro} con id {id_libro} creado con exito",
            "status": code

        }

    except Exception as e:
        print("Ocurrió un error al insertar, detalle del error: ", e)
        raise HTTPException(status_code=401, detail=f"Se produjo un error al insertar el libro, Detalle de error: {e}")

@app.get("/get_libros/", status_code=status.HTTP_200_OK)
def obtener_libros():
    """
    Función para obtener los libros

    Returns:
        libros (list): Lista de libros y sus versiones

    exepction:
        message (str): Mensaje de error al obtener los libros

    """
    code = False
    conexion = connectdb()
    cursor = conexion.cursor()
    try:
        query = f"SELECT * FROM libro"
        print(query)
        cursor.execute(query)
        libros = cursor.fetchall()
        data = []
        for libro in libros:
            item = {}
            # Verificar que la tupla libro tenga al menos un elemento
            if libro and len(libro) > 0:
                # Imprimir la tupla libro
                print(libro)
                for i in range(len(libro)):
                    item[cursor.description[i][0]] = libro[i]
                data.append(item)
                # obtener las versiones de los libros
                query = f"SELECT * FROM versiones WHERE id_libr = {libro[0]}"
                cursor.execute(query)
                versiones = cursor.fetchall()
                item["versiones"] = []
                for version in versiones:
                    item_version = {}
                    for i in range(len(version)):
                        item_version[cursor.description[i][0]] = version[i]
                        # quitar el id del libro de la version
                        if cursor.description[i][0] == "id_libro":
                            del item_version[cursor.description[i][0]]
                    item["versiones"].append(item_version)

        conexion.close()
        code = True
        return {
            "mensaje": "Libros obtenidos con exito",
            "libros": data,
            "status": code
        }

    except Exception as e:
        print("Ocurrió un error al obtener los libros, detalle del error: ", e)
        raise HTTPException(status_code=500, detail={"mensaje": f"Se produjo un error al obtener los libros, Detalle de error: {e}",
                                                     "status": code
                                                     } )



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", reload=True)