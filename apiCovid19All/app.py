from flask import Flask, jsonify, request
import requests
import datetime
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GHgsfvxhwdcXFty"#&/()=)'

def generate_token():
    time = datetime.datetime.utcnow()
    print(f"Time: {time}")
    plus_time= datetime.timedelta(minutes=5)
    print(f"plus_time: {plus_time}")
    expiration_time = time + plus_time
    print(f"Expiration time: {expiration_time}")
    payload = {'exp': expiration_time, 'iat': datetime.datetime.utcnow()}
    print(payload)
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired.'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token.'}

@app.route('/login')
def login():
    token = generate_token()
    return jsonify({'token': token})

@app.route('/get_covid_data')
def get_covid_data():
    global status
    try:
        token = request.args.get('token')
        if not token:
            return jsonify({'error': 'Token is missing.'})

        payload = verify_token(token)
        if 'error' in payload:
            return jsonify(payload)

        api_url = 'https://disease.sh/v3/covid-19/all'
        response = requests.get(api_url)
        data = response.json()

        if 'cases' not in data:
            return jsonify({'error': 'Data structure does not match expectations.'})

        # Create a dictionary with the data you want to display
        covid_data = {
            'casos': '{:,}'.format(data['cases']),
            'Recuperados':'{:,}'.format(data['recovered']),
            'RecuperadosHoy': '{:,}'.format(data['todayRecovered']),
            'Fallecidos': '{:,}'.format(data['deaths']),
            'CasosHoy': '{:,}'.format(data['todayCases']),
            'FallecidosHoy': '{:,}'.format(data['todayDeaths']),
            'CasosActivos': '{:,}'.format(data['active']),
            'CasosCríticos': '{:,}'.format(data['critical']),
            'TotalPruebas': '{:,}'.format(data['tests'])
        }
        status = True
        return jsonify({'Resumen_Covid_19': covid_data,
                        'status': status,
                        'message': 'Datos obtenidos correctamente'})

    except Exception as e:
        return jsonify({'Error al obtener los datos del Covid19': str(e),
                        'status': False})

if __name__ == '__main__':
    app.run()
