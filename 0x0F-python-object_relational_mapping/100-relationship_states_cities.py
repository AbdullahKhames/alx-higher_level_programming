#!/usr/bin/python3
"""
module to load all cities
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


def getSession(userName, pwd, dbName):
    """
    get session
    """
    engine = create_engine(f'mysql://{userName}:{pwd}@localhost:3306/{dbName}')
    Base.metadata.create_all(engine)
    return Session(bind=engine)


def createStateWithCities(userName, pwd, dbName):
    """
    createStateWithCities
    """
    session = getSession(userName, pwd, dbName)
    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)
    session.add_all([state, city])
    session.commit()
    states = session.query(State).all()
    for state in states:
        print("id  name")
        print(f"{state.id:<4}{state.name}")
        for city in state.cities:
            print("id  name    state_id")
            print(f"{city.id:<4}{city.name:}   {city.state_id}")


if __name__ == '__main__':
    """
    retrieve States
    """
    engine = create_engine('mysql://root:1395760@localhost:3306/hbtn_0e_6_usa')
    Base.metadata.create_all(engine)
    createStateWithCities(argv[1], argv[2], argv[3])
