import pandas as pd  # import pandas library
import json
from api_tabla_hobby.conexion_db import connectdb

df = pd.read_csv('panda.csv')  # read csv file


def insertar_datos_csv():
    """
    Insert data from csv file into database
    Returns:
        None
    """
    con = connectdb()  # conecta a la base de datos
    if not con:
        print(json.dumps("Error al conectar a la base de datos"))
        exit()
    cur = con.cursor()  # crea el cursor
    for index, row in df.iterrows():  # Itera sobre el DataFrame y mapea los valores de cada fila

        email = row["email"]  # Mapea el valor de la columna email
        nombre = row["name"]  # Mapea el valor de la columna name
        apellidos = row["lastname"]  # Mapea el valor de la columna lastname
        password = row["password"]  # Mapea el valor de la columna pass
        query = f"INSERT INTO usuarios (nombre, apellidos, email, password) values ( '{nombre}', '{apellidos}', " \
                f"'{email}', '{password}')"  # Query para insertar los datos
        cur.execute(query)  # Ejecuta el query
        con.commit()  # Confirma la transacción

    print("Datos insertados correctamente")
    con.close()  # Cierra la conexión
    cur.close()  # Cierra el cursor


if __name__ == '__main__':  # Si el archivo es ejecutado directamente
    try:
        insertar_datos_csv()  # Ejecuta la función insertar_datos_csv
    except Exception as e:
        print("Ocurrió un error al insertar los datos: ", e)
        exit()

