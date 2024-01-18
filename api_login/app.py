import psycopg2
from flask import Flask, request, jsonify, render_template, session
from connection_db import connectdb
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='/static', static_folder='static')
cors = CORS(app)
app.secret_key = 'mysecretkey'  # Clave secreta para la gestión de sesiones

@app.route('/')
def home():
    return render_template('login_form.html')

@app.route('/dashboard.html')
def dashboard():
    # Code to render the dashboard template or perform other actions
    return render_template('dashboard.html')


# Ruta para procesar los datos del formulario de inicio de sesión
@app.route('/login', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def process_login():
    data = request.get_json()  # Obtener datos enviados como JSON

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': "Ingresa los campos email y password."})

    else:

    # Realiza la consulta en la base de datos MySQL
        try:
            conn = connectdb()
            if isinstance(conn, psycopg2.OperationalError):
                raise Exception(f"Error en la conexión a la base de datos: {conn}")
            cursor = conn.cursor()
            query = f"select * from usuarios where email = '{email}' and password = '{password}'"
            print("Se hace consulta a la base de datos")
            print(query)
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"Usuario encontrado: {result}")
            conn.close()
            cursor.close()

            if result:
                user = result[0]
                session['username'] = user[1]
                return jsonify({'success': True, 'message': f"Inicio de sesión exitoso. Bienvenido, {user[1]}."})
            else:
                return jsonify({'success': False, 'message': "Inicio de sesión fallido. Usuario no encontrado."})


        except Exception as err:
            return jsonify({'success': False, 'message': str(err)})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)

