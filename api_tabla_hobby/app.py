import json
from conexion_db import connectdb
from flask import Flask, jsonify, request
from flask_cors import cross_origin, CORS

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/usuarios', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_usuarios():
    # Establecer conexión con la base de datos
    con = connectdb()
    output = {'response': False}
    cursor = con.cursor()
    usuarioArray = []
    hijoArray = []
    hobbyArray = []
    enfermedadArray = []
    relojesArray = []
    mascotasArray = []

    cursor.execute("select * from usuarios order by id_usuario")
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
                            if id_usuario == hijo[1]:
                                cursor.execute("select * from relojes")
                                relojes = cursor.fetchall()
                                for reloj in relojes:
                                    id_reloj = reloj[0]
                                    marca_reloj = reloj[2]
                                    modelo_reloj = reloj[3]
                                    if id_hijo == reloj[1]:
                                        relojesArray.append({
                                            'id_reloj': id_reloj,
                                            'marca_reloj': marca_reloj,
                                            'modelo_reloj': modelo_reloj
                                        })

                hijoArray.append({
                    'id_hijo': id_hijo,
                    'nombre': nombre_hijo,
                    'apellido': apellido_hijo,
                    'hobbies': hobbyArray,
                    'enfremedades': enfermedadArray,
                    'relojes': relojesArray
                })

                hobbyArray = []
                enfermedadArray = []
                relojesArray = []

        cursor.execute("select * from mascotas")
        mascotas = cursor.fetchall()
        for mascota in mascotas:
            id_mascota = mascota[0]
            tipo_mascota = mascota[2]
            nombre_mascota = mascota[3]
            if id_usuario == mascota[1]:
                mascotasArray.append({
                    'id_mascota': id_mascota,
                    'tipo': tipo_mascota,
                    'nombre': nombre_mascota

                })

        usuarioArray.append({
            'id_usuario': id_usuario,
            'nombres': nombre_usuario,
            'apellido': apellido_usuario,
            'usuario': usuario,
            'mascotas': mascotasArray,
            'hijos': hijoArray,

        })

        hijoArray = []
        mascotasArray = []

    output['message'] = 'Se obtuvieron correctamente los items'
    output['response'] = True

    json_data = json.dumps(usuarioArray, indent=4)
    print(str("Usuarios:"), json_data)
    return jsonify("Usuarios:", usuarioArray, output)


if __name__ == '__main__':
    app.run(debug=True)

