import pymysql
from flask import Flask, request, render_template, redirect, url_for, session
from connection_db import connectdb

app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Clave secreta para la gestión de sesiones

# Ruta para mostrar el formulario de inicio de sesión
@app.route('/')
def show_login_form():
    error = session.pop('error', None)
    success = session.pop('success', None)
    return render_template('login_form.html', error=error, success=success)

# Ruta para procesar los datos del formulario de inicio de sesión
@app.route('/login', methods=['POST'])
def process_login():
    email = request.form['email']
    password = request.form['password']

    # Realiza el registro de los datos en la base de datos MySQL
    try:
        conn = connectdb()
        if isinstance(conn, pymysql.err.OperationalError):
            raise Exception(f"Error en la conexión a la base de datos: {conn}")

        cursor = conn.cursor()
        query = f"select * from usuarios where email = '{email}' and password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            user = result[0]  # Obtenemos el primer registro de la lista (la primera tupla)
            session[
                'success'] = f"Inicio de sesión exitoso. Bienvenido, {user[1]}."  # Asumiendo que el campo 'nombre' está en la posición 1 de la tupla
            return redirect(url_for('show_login_form'))
        else:
            session['error'] = "Usuario o credenciales incorrectas. Vuelve a intentarlo."
            return redirect(url_for('show_login_form'))



    except Exception as err:
        return str(err)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

