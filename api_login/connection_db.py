import psycopg2

def connectdb():
    """
    Connect to database
    Returns:
        con: connection
        raise Exception: if connection fails
        False: if connection fails
    """

    try:
        conexion = psycopg2.connect(host='localhost',
                                    user='postgres',
                                    password='lALOFER1982',
                                    dbname='safdb')

        return conexion

    except (psycopg2.OperationalError, psycopg2.InternalError) as e:
        print("Ocurrió un error al conectar, detalle del error: ", e)
        return e
