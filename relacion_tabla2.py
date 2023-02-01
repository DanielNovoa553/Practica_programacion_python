
import json
from conexion_db import connectdb

# Establecer conexión con la base de datos
con = connectdb()
cursor = con.cursor()


# Consultar los datos de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Consultar los datos de la tabla de pedidos
cursor.execute("SELECT * FROM hijos")
hijos = cursor.fetchall()

# Crear un diccionario para almacenar la relación entre clientes y pedidos
relacion = {}

# Recorrer los datos de la tabla de clientes
for usuario in usuarios:
    id_usuario = usuario[0]
    nombre_usurio = usuario[1]
    apellido_usuario = usuario[2]
    relacion[id_usuario] = {'id_usuario': id_usuario, 'nombres': nombre_usurio, 'apellido': apellido_usuario, 'hijos': []}

# Recorrer los datos de la tabla de pedidos
for hijo in hijos:
    id_hijo = hijo[0]
    id_usuario= hijo[1]
    nombre_hijo = hijo[2]
    apellido_hijo = hijo[3]
    relacion[id_usuario]['hijos'].append({'id_hijo': id_hijo, 'nombre': nombre_hijo, 'apellido': apellido_hijo})

# Convertir el diccionario a formato JSON
json_data = json.dumps(relacion, indent=4)

# Imprimir los datos en formato JSON
print(json_data)

# Cerrar la conexión a la base de datos
con.close()
