#!/usr/bin/python3

"""
to demonstrate mysql db connection using DBAPI called MySQLdb
"""
from sys import argv
import MySQLdb


def getCities(uName, pwd, dbName):
    """
    getCities function
    """
    dv = MySQLdb.connect(host='localhost',
                         user=uName,
                         passwd=pwd,
                         database=dbName,
                         port=3306)
    sql_query = 'SELECT c.id, c.name, s.name \
        FROM cities c \
        INNER JOIN states s\
        ON s.id = c.state_id\
        ORDER BY c.id ASC'
    cur = dv.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    """
    prevents script from running when imported
    """
    getCities(argv[1], argv[2], argv[3])
