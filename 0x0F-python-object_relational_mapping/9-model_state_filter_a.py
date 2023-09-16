#!/usr/bin/python3


"""
module to load all states
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def getSession(userName, pwd, dbName):
    """
    get session
    """
    engine = create_engine(f'mysql://{userName}:{pwd}@localhost:3306/{dbName}')
    return Session(bind=engine)


def retrieveStates(userName, pwd, dbName):
    """
    retrieve States
    """
    session = getSession(userName, pwd, dbName)
    for state in session.query(State).filter(State.name.like("%a%")).order_by(State.id).all():
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    """
    retrieve States
    """
    retrieveStates(argv[1], argv[2], argv[3])
