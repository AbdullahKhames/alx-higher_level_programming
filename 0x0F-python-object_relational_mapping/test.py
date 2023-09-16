#!/usr/bin/env python3

from sqlalchemy import create_engine, MetaData,text
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import DateTime, ForeignKey, inspect, and_, or_
from sqlalchemy.orm import declarative_base, Session
Base = declarative_base()

class Network(Base):
    __tablename__ = 'networks2'
    id = Column(Integer, primary_key=True)
    name =  Column(String(100), nullable=False)


def run_query():
    engine = create_engine("mysql://root:1395760@localhost/test")
    con = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables['app_users']
    select_statement = table.select().where(or_(table.c.name == 'edward', and_(table.c.fullname == 'ed', table.c.id > 5)))
    print(select_statement)
    result = con.execute(select_statement)
    rows = result.fetchall()
    for row in rows:
        print(row)
    con.commit()

def orm():
    engine = create_engine("mysql://root:1395760@localhost/test")
    Base.metadata.create_all(engine)
    network1 = Network(name='first')
    network2 = Network(name='second')
    network3 = Network(name='third')
    network4 = Network(name='fourth')
    session = Session(bind=engine)
    session.add_all([network1, network2, network3, network4])
    for name in session.query(Network):
        print(name.name)


if __name__ == '__main__':
    orm()
