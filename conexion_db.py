import pymysql


def connectdb():
    """
    This function connect to a database
    Returns:
        con: connection to database

    """
    return pymysql.connect(host='localhost',
                           port=3306,
                           db='plasticos',
                           user='root',
                           password='Lalofer1982',
                           )
