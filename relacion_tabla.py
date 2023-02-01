
import json
from conexion_db import connectdb

# Establecer conexión con la base de datos
con = connectdb()
cursor = con.cursor()
# Ejecutar SELECT para obtener los datos de clientes y pedidos
query = "select * from usuarios inner join hijos on usuarios.id_usuario = hijos.id_usuario;"
cursor.execute(query)

# Almacenar los resultados en una lista
results = cursor.fetchall()

# Crear un diccionario para almacenar los datos
data = {}

# Iterar sobre los resultados y agregarlos al diccionario
for result in results:
    usuario_id = result[0]

    usuario_nombre = result[1]
    usuario_apellido = result[2]
    usuario = result[3]
    id_hijo = result[4]
    nombre_hijo = result[6]
    apellido_hijo = result[7]

    if usuario_id not in data:  # Si el usuario no está en el diccionario
        data[usuario_id] = {    # Agregar el usuario al diccionario

            'nombres': usuario_nombre,   # Agregar el nombre del usuario
            'apellidos': usuario_apellido,   # Agregar el apellido del usuario
            'usuario': usuario,  # Agregar el usuario
            'hijos': []
        }

    data[usuario_id]['hijos'].append({  # Agregar el hijo al diccionario
        'id_hijo': id_hijo,     # Agregar el id del hijo
        'nombres_hijo': nombre_hijo,    # Agregar el nombre del hijo
        'apellidos_hijo': apellido_hijo     # Agregar el apellido del hijo
    })

# Convertir el diccionario a JSON
json_data = json.dumps(data, indent=4)

# Imprimir el JSON
print(json_data)

# Cerrar la conexión con la base de datos
con.close()
