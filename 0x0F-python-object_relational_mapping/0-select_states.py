#!/usr/bin/python3

"""
to demonstrate mysql db connection using DBAPI called MySQLdb
"""
from sys import argv
import MySQLdb


def connect(uName, pwd, dbName):
    """
    connection function
    """
    dv = MySQLdb.connect(host='localhost', user=uName, password=pwd,
                         database=dbName, port=3306)
    sql_query = 'SELECT * FROM states s ORDER BY s.id ASC'
    cur = dv.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    """
    prevents script from running when imported
    """
    connect(argv[1], argv[2], argv[3])
