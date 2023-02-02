import json
from conexion_db import connectdb

# Establecer conexión con la base de datos
con = connectdb()  # <--- Aquí se llama a la función connectdb() del archivo conexion_db.py
cursor = con.cursor()   # <--- Aquí se crea el cursor
usuarioArray = []   # <--- Aquí se crea un array vacío para almacenar los datos de los usuarios
hijoArray = []  # <--- Aquí se crea un array vacío para almacenar los datos de los hijos
cursor.execute("select * from usuarios ") # <--- Aquí se ejecuta la consulta para obtener los datos de los usuarios
usuarios = cursor.fetchall()    # <--- Aquí se almacenan los resultados de la consulta en una variable


for usuario in usuarios:    # <--- Aquí se itera sobre los resultados de la consulta
    id_usuario = usuario[0]     # <--- Aquí se obtiene el id del usuario
    nombre_usuario = usuario[1]    # <--- Aquí se obtiene el nombre del usuario
    apellido_usuario = usuario[2]
    usuario = usuario[3]
    # <--- Aquí se obtiene el apellido del usuario

    cursor.execute("select * from hijos")   # <--- Aquí se ejecuta la consulta para obtener los datos de los hijos
    hijos = cursor.fetchall()       # <--- Aquí se almacenan los resultados de la consulta en una variable

    for hijo in hijos:    # <--- Aquí se itera sobre los resultados de la consulta
        id_hijo = hijo[0]   # <--- Aquí se obtiene el id del hijo
        nombre_hijo = hijo[2]   # <--- Aquí se obtiene el nombre del hijo
        apellido_hijo = hijo[3]    # <--- Aquí se obtiene el apellido del hijo
        if id_usuario == hijo[1]:       # <--- Aquí se verifica si el id del usuario es igual al id del usuario de la tabla hijos
            hijoArray.append({    # <--- Aquí se agrega el hijo al array hijoArray
                'id_hijo': id_hijo,    # <--- Aquí se agrega el id del hijo
                'nombre': nombre_hijo,  # <--- Aquí se agrega el nombre del hijo
                'apellido': apellido_hijo})  # <--- Aquí se agrega el apellido del hijo
        if hijoArray == []:
            hijoArray = False
    usuarioArray.append({   # <--- Aquí se agrega el usuario al array usuarioArray
        'id_usuario': id_usuario,   # <--- Aquí se agrega el id del usuario
        'nombres': nombre_usuario,      # <--- Aquí se agrega el nombre del usuario
        'apellido': apellido_usuario, # <--- Aquí se agrega el apellido del usuario
        'usuario': usuario,   # <--- Aquí se agrega el nombre de usuario
        'hijos': hijoArray  # <--- Aquí se agrega el array hijoArray al array usuarioArray
    })

    hijoArray = [] # <--- Aquí se vacía el array hijoArray

# <--- Aquí se agrega el array usuarioArray al array relacion_tabla

# Convertir el diccionario a formato JSON
json_data = json.dumps(usuarioArray, indent=4) # <--- Aquí se convierte el array usuarioArray a formato JSON

# Imprimir los datos en formato JSON
print('usuarios:',json_data)

# Cerrar la conexión a la base de datos
con.close()
cursor.close()
