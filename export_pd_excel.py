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

    try:
        query = "SELECT * FROM usuarios"  # Query to select data
        cur.execute(query)  # Execute query
        results = cur.fetchall()  # Fetch all data

        df = pd.DataFrame(results, columns=["id", "nombres", "apellidos", "usuario"])  # Create dataframe

        profit = df['profit'] = df['id'] * 1000000.34 / 2.5  # Add date column
        profit = pd.Series(profit)  # Convert to series to apply lambda function
        profit = profit.apply(lambda x: "{:,.2f}".format(x))  # Replace . with ,
        df['profit'] = profit  # Add profit column to dataframe

        # Export dataframe to excel
        writer = pd.ExcelWriter("C:/Users/danie/OneDrive/Documentos/Balance_Profit_Users/datos.xlsx")  # create xlsx file
        df.to_excel(writer, "datos_" + date, index=False, header=True, freeze_panes=(1, 0),
                    engine='xlswriter')  # write data to xlsx file
        #   print(df)
        worksheet = writer.sheets['datos_' + date]  # Get worksheet
        worksheet.set_column(0, 0, 5)
        worksheet.set_column(1, 1, 20)
        worksheet.set_column(2, 2, 20)
        worksheet.set_column(3, 3, 15)
        worksheet.set_column(4, 4, 15)

        fileName = os.path.abspath(
            "C:/Users/danie/OneDrive/Documentos/Balance_Profit_Users/datos.xlsx")  # Get absolute path of file
        os.startfile(fileName)  # Open file
        print("Datos exportados exitosamente a --> datos.xlsx")

        con.close()  # Close connection
        cur.close()  # Close cursor
        writer.close()  # writer close
    except Exception as e:
        print("Ocurrió un error al exportar los datos: ", e)
        exit()


if __name__ == '__main__':  # If file is executed directly

    exportar_datos_excel()  # Execute function exporta datos a excel
