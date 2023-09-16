#!/usr/bin/python3

"""
to demonstrate mysql db connection using DBAPI called MySQLdb
"""
from sys import argv
import MySQLdb


def searchStates(uName, pwd, dbName, searched):
    """
    searchStates function
    """
    dv = MySQLdb.connect(host='localhost',
                         user=uName,
                         passwd=pwd,
                         database=dbName,
                         port=3306)
    sql_query = 'SELECT * FROM states s WHERE \
        s.name = \"{}\" ORDER BY s.id ASC'.format(searched)
    cur = dv.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dv.close()


if __name__ == '__main__':
    """
    prevents script from running when imported
    """
    searchStates(argv[1], argv[2], argv[3], argv[4])
