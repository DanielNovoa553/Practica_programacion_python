import xlwt
from api_tabla_hobby.conexion_db import connectdb
import os


def export_to_excel():
    # connect to the database
    conexion = connectdb()

    # create a cursor object
    cursor = conexion.cursor()

    # create a workbook
    workbook = xlwt.Workbook()

    # create a worksheet
    worksheet = workbook.add_sheet('data')

    # execute the query
    cursor.execute('SELECT * FROM usuarios')

    row = 0

    # write the data to the worksheet
    for id, name, email, password in cursor.fetchall():
        worksheet.write(row, 0, id)
        worksheet.write(row, 1, name)
        worksheet.write(row, 2, email)
        worksheet.write(row, 3, password)
        row += 1

    # save the xls file
    workbook.save('data.xls')
    file = os.path.abspath("data.xls")  # Get absolute path of file
    os.startfile(file)  # Open file
    # close the cursor
    cursor.close()

    # close the connection
    conexion.close()

    # display a message
    print('Data has been exported to data.xls')

    # close the program
    exit()


if __name__ == '__main__':
    try:
        export_to_excel()
    except Exception as e:
        print("Ocurrió un error al exportar los datos: ", e)
        exit()
