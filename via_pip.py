import os
import pandas as pd
import glob


# Ruta con el patrón del archivo en el escritorio
ruta_patron = 'C:\\Users\\danie\\OneDrive\\Escritorio\\VIA*.pip'

# Obtener la lista de archivos que coinciden con el patrón
archivos_encontrados = glob.glob(ruta_patron)

# Verificar si se encontraron archivos
if archivos_encontrados:
    # Tomar el primer archivo encontrado
    archivo_ruta = archivos_encontrados[0]

    try:
        with open(archivo_ruta, 'r') as archivo:
            # Lee líneas del archivo y crea una lista
            lineas = archivo.readlines()
            if not archivo:
                print("El archivo está vacío.")
            # Extraer información de cada línea en campos específicos
            else:
                datos = []
                for linea in lineas:
                    fecha_linea = linea[0:8]
                    tipo = linea[8:10]
                    codigo = linea[10:19]
                    client = linea[19:25]
                    valor = linea[25:].strip()

                    # Realiza la concatenación específica para 'Codigo_Categoria'
                    client_id = f"{tipo}_{codigo}_{client}".replace(" ", "").replace("__", "_")

                    # Crea la nueva línea de datos
                    nueva_linea = [fecha_linea, tipo, codigo, client, valor, client_id]
                    datos.append(nueva_linea)

                # Crear un DataFrame de pandas
                columnas = ['Fecha', 'Tipo', 'Codigo', 'Categoria', 'Valor', 'CLIENT_ID']
                df = pd.DataFrame(datos, columns=columnas, index=None)

                # Crea la columna 'moneda_emision' con los dos últimos dígitos de 'Valor'
                df['MONEDA EMISION'] = df['Valor'].str[-2:]

                # Mapear lo moneda de emición usando un diccionario llamado monedas
                monedas = {
                    'MX': 'MXN',
                    '*M': 'MXN',
                    '*N': 'MXN',
                    'US': 'USD',
                    'GB': 'GBP',
                    'JP': 'JPY',
                    'EU': 'EUR',
                          }

                # Reemplazar los valores de la columna 'moneda_emision' con los valores del diccionario
                df['MONEDA EMISION'] = df['MONEDA EMISION'].replace(monedas)

                # solo dejar las columnas codigo_categoria y moneda_emision
                df = df[['CLIENT_ID', 'MONEDA EMISION']]
                # quitar la columna index

                # imprimir el DataFrame sin el índice
                print(df)

                # Guardar el DataFrame en un archivo CSV
                df.to_csv('C:\\Users\\danie\\OneDrive\\Escritorio\\VIA_pip.csv', index=False)

                # abrir el archivo CSV con Excel
                os.system('start excel.exe "C:\\Users\\danie\\OneDrive\\Escritorio\\VIA_pip.csv"')

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
else:
    print("No se encontraron archivos que coincidan con el patrón.")

