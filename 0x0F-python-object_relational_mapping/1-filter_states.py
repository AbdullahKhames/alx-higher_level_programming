#!/usr/bin/python3

"""
to demonstrate mysql db connection using DBAPI called MySQLdb
"""
from sys import argv
import MySQLdb


def filterStates(uName, pwd, dbName):
    """
    filterStates function
    """
    dv = MySQLdb.connect(host='localhost', user=uName, password=pwd,
                         database=dbName, port=3306)
    try:
        sql_query = "SELECT * FROM states s\
            WHERE s.name LIKE 'N%' ORDER BY s.id ASC"
        cur = dv.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        cur.close()
        dv.close()


if __name__ == '__main__':
    """
    prevents script from running when imported
    """
    filterStates(argv[1], argv[2], argv[3])
