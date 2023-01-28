# hacer un programa con pandas que lea una base de datos mysql y exporte los datos a un archivo excel
import datetime

import pandas as pd
import os
from conexion_db import connectdb
from datetime import datetime

def exportar_datos_excel():
    """
    Export data from database to excel file
    Returns:
        None
    """
    x = datetime.now()
    date = x.strftime("%d_%m_%Y_%H_%M_%S")
    print(date)
    con = connectdb()  # connect to database
    if not con:
        print("Error al conectar a la base de datos")
        exit()
    cur = con.cursor()  # create cursor
    query = "SELECT * FROM usuarios"  # Query to select data
    cur.execute(query)  # Execute query
    results = cur.fetchall()  # Fetch all data

    # Create dataframe
    df = pd.DataFrame(results, columns=["id", "nombres", "apellidos", "usuario"])

    # Export dataframe to excel
    writer = pd.ExcelWriter("datos.xlsx")
    df.to_excel(writer, "datos_"+date, index=False, header=True, freeze_panes=(1, 0))
    writer.close()

    # Open file
    file = os.path.abspath("datos.xlsx")  # Get absolute path of file
    os.startfile(file)  # Open file
    print("Datos exportados exitosamente a --> datos.xlsx ")
    con.close()  # Close connection
    cur.close()  # Close cursor


if __name__ == '__main__':  # If file is executed directly
    try:
        exportar_datos_excel()  # Execute function exportar_datos_excel
    except Exception as e:
        print("Ocurrió un error al exportar los datos: ", e)
        exit()
