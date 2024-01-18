import pandas as pd

# Read the CSV file
def readExcel():
    # read xlsx file
    df = pd.read_excel('C:/Users/danie/OneDrive/Escritorio/Proyecto_AMMA/DEMO_ALMACEN_AMMA.xlsx')
    # set the display format
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #set decimal format to integer
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    # print the dataframe
    print(df)

if __name__ == '__main__':
    readExcel()