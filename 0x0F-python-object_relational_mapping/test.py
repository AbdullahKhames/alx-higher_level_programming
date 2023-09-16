#!/usr/bin/env python3

from sqlalchemy import create_engine, text



def run_query():
    engine = create_engine("mysql://root:@localhost/test")
    
    sql_query = text("SELECT * FROM employee")

    with engine.connect() as connection:
        result = connection.execute(sql_query)

        for row in result:
            print(row)

if __name__ == '__main__':
    run_query()
