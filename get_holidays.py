import holidays
from catalogo_holidays import rename_holidays

# Cargar feriados para México
mx_holidays = holidays.MX(years=2024, observed=False)
i = 0
# Diccionario de nombres de feriados

# renombrar feriados usando diccionario
renamed_holidays = {rename_holidays[v]: k for k, v in mx_holidays.items()} #

# Imprimir nuevos nombres de feriados
for k, v in renamed_holidays.items():
    i += 1
    print(f"Feriado # {i}, Fecha: {v}: {k}")

#serializar el diccionario a un archivo json para su posterior uso en el programa principal de la aplicación y mostrar por pantalla
import json
data = json.dumps(renamed_holidays, indent=4, default=str, ensure_ascii=False)
print(data)
print(f"Total de feriados: {len(renamed_holidays)}")
print("!!!Fin del programa!!!")
exit()