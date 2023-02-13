numero = 1000000
cadena = '{:,.2f}'.format(numero)
print(cadena)

import pandas as pd

# Crear una serie con el número 10000000.00
numero = pd.Series([10000000.00])

# Aplicar la función de formato a la serie
numero_formateado = numero.apply(lambda x: "{:,.2f}".format(x))

# Imprimir el resultado
print(numero_formateado)