#!/usr/bin/python3

"""
to demonstrate mysql db connection using DBAPI called MySQLdb
"""
from sys import argv
import MySQLdb


def getConnection(uName, pwd, dbName, stateName):
    return MySQLdb.connect(host='localhost',
                         user=uName,
                         passwd=pwd,
                         database=dbName,
                         port=3306)


def displayRows(rows):
    first_iteration = True
    for row in rows:
        if not first_iteration:
            print(", ", end="")
        print(row[0], end="")
        first_iteration = False
    print()


def filteredCities(uName, pwd, dbName, stateName):
    """
    filteredCities function
    """
    dv = getConnection(uName, pwd, dbName, stateName)
    sql_query = 'SELECT c.name \
        FROM cities c \
        INNER JOIN states s \
        ON s.id = c.state_id \
        WHERE s.name = "{}"\
        ORDER BY c.id ASC'.format(stripSearchedStr(stateName))
    cur = dv.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    displayRows(rows)
    cur.close()
    dv.close()


def stripSearchedStr(searched):
    return searched.split(';')[0]


if __name__ == '__main__':
    """
    prevents script from running when imported
    """
    filteredCities(argv[1], argv[2], argv[3], argv[4])
