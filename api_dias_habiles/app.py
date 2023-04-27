import json
from flask import Flask, jsonify
import pandas as pd
from datetime import date
from flask_cors import cross_origin, CORS

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/dias_habiles', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_holidays():
# Definir rango de fechas
    fecha_inicio = date(2023, 2, 1)
    fecha_fin = date(2023, 2, 7)
    output = {'response': False}
    # Crear lista de fechas
    rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='D').to_pydatetime().tolist()

    # Identificar días hábiles y no hábiles
    calendario = pd.DataFrame({'fecha': rango_fechas})
    calendario['no_habil'] = calendario['fecha'].dt.dayofweek.isin([5, 6])


    #mapear los no hábiles y habiles en un diccionario
    dias = {
            "Monday": "Lunes",
            "Tuesday": "Martes",
            "Wednesday": "Miércoles",
            "Thursday": "Jueves",
            "Friday": "Viernes",
            "Saturday": "Sábado",
            "Sunday": "Domingo",
     }

    # Imprimir días hábiles y no hábiles del nuevo diccionario
    for i, row in calendario.iterrows():
        fecha = row['fecha'].strftime('%Y-%m-%d')
        dia_semana = row['fecha'].strftime('%A')
        if row['no_habil']:
            print(f'{dias[dia_semana]} {fecha}: NO es un día hábil')
        else:
            print(f'{dias[dia_semana]} {fecha}: es un día hábil')

    semanaArray = []
    contenedorArray = []
    for i, row in calendario.iterrows():
        fecha = row['fecha'].strftime('%Y-%m-%d')
        dia_semana = row['fecha'].strftime('%A')
        if row['no_habil']:
            semanaArray.append({
                'fecha': fecha,
                'dia_semana': dias[dia_semana],
                'no_habil': True
            })
        else:
            semanaArray.append({
                'fecha': fecha,
                'dia_semana': dias[dia_semana],
                'no_habil': False
            })
    contenedorArray.append({
        'Dias': semanaArray
    })
    json_data = json.dumps(contenedorArray, indent=4, default=str, ensure_ascii=False)
    print(str("Semana:"), json_data)
    output['response'] = True
    output['Semana'] = contenedorArray
    output['message'] = 'Días hábiles y no hábiles cargados correctamente'
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
