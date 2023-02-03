import json
from conexion_db import connectdb

# Establecer conexión con la base de datos
con = connectdb()
cursor = con.cursor()
usuarioArray = []
hijoArray = []
hobbyArray = []
enfermedadArray = []

cursor.execute("select * from usuarios ")
usuarios = cursor.fetchall()

for user in usuarios:

    id_usuario = user[0]
    nombre_usuario = user[1]
    apellido_usuario = user[2]
    usuario = user[3]
    cursor.execute("select * from hijos")
    hijos = cursor.fetchall()
    for hijo in hijos:
        id_hijo = hijo[0]
        nombre_hijo = hijo[2]
        apellido_hijo = hijo[3]
        if id_usuario == hijo[1]:
            cursor.execute("select * from hobby")
            hobbies = cursor.fetchall()
            for hobby in hobbies:
                id_hobby = hobby[0]
                nombre_hobby = hobby[2]
                if id_hijo == hobby[1]:
                    hobbyArray.append({
                        'id_hobby': id_hobby,
                        'nombre': nombre_hobby
                    })
            if id_usuario == hijo[1]:
                cursor.execute("select * from enfermedad")
                enfermedades = cursor.fetchall()
                for enfermedad in enfermedades:
                    id_enfermedad = enfermedad[0]
                    nombre_enfermedad= enfermedad[2]
                    if id_hijo == enfermedad[1]:
                        enfermedadArray.append({
                            'id_enfermedad': id_enfermedad,
                            'nombre_enfermedad': nombre_enfermedad
                        })
            hijoArray.append({
                'id_hijo': id_hijo,
                'nombre': nombre_hijo,
                'apellido': apellido_hijo,
                'hobbies': hobbyArray,
                'enfremedades': enfermedadArray
            })

            hobbyArray = []
            enfermedadArray = []

    usuarioArray.append({
        'id_usuario': id_usuario,
        'nombres': nombre_usuario,
        'apellido': apellido_usuario,
        'usuario': usuario,
        'hijos': hijoArray
    })
    hijoArray = []

json_data = json.dumps(usuarioArray, indent=4)
print('Usuarios:', json_data)
