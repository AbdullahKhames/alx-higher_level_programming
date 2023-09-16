#!/usr/bin/env python3

from sqlalchemy import create_engine, text


def run_query():
    engine = create_engine("mysql://root:1395760@localhost/test")
    

    with engine.connect() as conn:
        result = conn.execute(text("INSERT INTO employee values(1, 'dilbert')"))
        result = conn.execute(text("SELECT * FROM employee"))
        rows = result.fetchall()
        for row in rows:
            print(row)

if __name__ == '__main__':
    run_query()
