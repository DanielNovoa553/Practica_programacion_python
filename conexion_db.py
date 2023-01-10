import pymysql


def connectdb():
    return pymysql.connect(host='localhost',
                           port=3306,
                           db='plasticos',
                           user='root',
                           password='Lalofer1982',
                           )
