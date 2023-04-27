# hacer una funcion que se conecte a una base de datos mysql y maneje excepciones
from fastapi import FastAPI, HTTPException

import pymysql


def connectdb():
    """
    Connect to database
    Returns:
        con: connection
        raise Exception: if connection fails
        False: if connection fails
    """

    global conexion
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   db='libros')

        return conexion

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar, detalle del error: ", e)
        raise HTTPException(status_code=503, detail=f"Error al conectar a la base de datos. Detalle del error: {e}")

