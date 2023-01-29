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
    x = datetime.now()  # Get current date and time
    date = x.strftime("%d_%m_%Y_%H_%M_%S")  # change format date to string

    con = connectdb()  # connect to database
    if not con: # If connection is not established
        print("Error al conectar a la base de datos")
        exit()  # Close program

    cur = con.cursor()  # create cursor
    query = "SELECT * FROM usuarios"  # Query to select data
    cur.execute(query)  # Execute query
    results = cur.fetchall()  # Fetch all data

    df = pd.DataFrame(results, columns=["id", "nombres", "apellidos", "usuario"])   # Create dataframe

    profit = df['profit'] = round((df['id'] * 100.34 / 2.5), 2)# Add date column
    profit = profit.astype(str)  # Convert to string
    profit = profit.apply(lambda x: x.replace('.', ','))    # Replace . with ,
    df['profit'] = profit # Add profit column to dataframe

    # Export dataframe to excel
    writer = pd.ExcelWriter("C:/Users/danie/OneDrive/Documentos/Balance_Profit_Users/datos.xlsx")   #create excel file
    df.to_excel(writer, "datos_"+date, index=False, header=True, freeze_panes=(1, 0), engine='csvwriter')   #write data to excel file
    print(df)

    fileName = os.path.abspath("C:/Users/danie/OneDrive/Documentos/Balance_Profit_Users/datos.xlsx")  # Get absolute path of file
    os.startfile(fileName)  # Open file
    print("Datos exportados exitosamente a --> datos.xlsx")

    con.close()  # Close connection
    cur.close()  # Close cursor
    writer.close() # writer close


if __name__ == '__main__':  # If file is executed directly
    try:
        exportar_datos_excel()  # Execute function exportar_datos_excel
    except Exception as e:
        print("Ocurrió un error al exportar los datos: ", e)
        exit()
