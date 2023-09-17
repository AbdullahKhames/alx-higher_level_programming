#!/usr/bin/python3


"""
module to load all cities
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, subqueryload
from model_state import Base, State
from model_city import City


def getSession(userName, pwd, dbName):
    """
    get session
    """
    engine = create_engine(f'mysql://{userName}:{pwd}@localhost:3306/{dbName}')
    return Session(bind=engine)


def fetchCitiesByState(userName, pwd, dbName):
    """
    update State
    """
    session = getSession(userName, pwd, dbName)
    query = session.query(State)\
                    .join(State.cities)\
                    .options(subqueryload(State.cities))\
                    .order_by(City.id)
    states = query.all()
    for state in states:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == '__main__':
    """
    retrieve States
    """
    fetchCitiesByState(argv[1], argv[2], argv[3])
