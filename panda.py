from Scripts.rst2odt import output

from conexion_db import connectdb # import the function connectdb from conexion_db.py
import pandas as pd  # import pandas library


def insertar_datos_csv():
    """
    This function insert data from a csv file into a database
    Args:
        None
    Returns:
        None
    """
    df = pd.read_csv('panda.csv')   # read csv file
    # print(df) # print dataframe

    # df_filtrado = df.dropna()   # Elimina las filas con valores nulos
    # print("\n", df_filtrado)    # Imprime el nuevo DataFrame
    #
    # df_remove = df.fillna(0)    # Reemplaza los valores nulos por 0
    # print("\n", df_remove)  # Imprime el nuevo DataFrame
    #
    # print("\n", df[["email", "name", "lastname"]])# Imprime las columnas email y name
    # df_iloc = df.iloc[0]    # Imprime la primera fila
    # print("\n", df_iloc)    # Imprime la primera fila
    #
    # df_fillna =df.fillna({"email":0, "pass": -1})# Reemplaza los valores nulos por 0 y -1
    # print("\n",df_fillna)   # Imprime el nuevo DataFrame
    #
    # df_registro = df.loc[[1], ["id", "email", "name", "lastname", "user", "pass"]] #
    # print("\n", df_registro)
    con = connectdb() # conecta a la base de datos
    cur = con.cursor() # crea el cursor
    for index, row in df.iterrows():    # Itera sobre el DataFrame y mapea los valores de cada fila

        email = row["email"]    # Mapea el valor de la columna email
        nombre = row["name"]    # Mapea el valor de la columna name
        apellidos = row["lastname"]  # Mapea el valor de la columna lastname
        password = row["password"]  # Mapea el valor de la columna pass
        query = f"INSERT INTO usuarios (nombre, apellidos, email, password) values ( '{nombre}', '{apellidos}', " \
                f"'{email}', '{password}')" # Query para insertar los datos
        cur.execute(query) # Ejecuta el query
        con.commit()  # Confirma la transacción


    print("Datos insertados correctamente")
    con.close()  # Cierra la conexión
    cur.close()  # Cierra el cursor


if __name__ == '__main__':
    insertar_datos_csv()


try:



    except Exception as e:
        print(e)
        print('Ocurrio un error al crear al usuario en la BD')
        output['message'] = 'Ocurrio un error al crear al usuario en la BD'
        return jsonify(output), 500