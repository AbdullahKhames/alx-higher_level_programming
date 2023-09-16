#!/usr/bin/python3


"""
module to load all states
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def getConnection(userName, pwd, dbName):
    """
    get connection
    """
    return create_engine(f'mysql://{userName}:{pwd}@localhost:3306/{dbName}')


def retrieveStates(userName, pwd, dbName):
    """
    retrieve States
    """
    engine = getConnection(userName, pwd, dbName)
    session = Session(bind=engine)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing ')
    else:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    """
    retrieve States
    """
    retrieveStates(argv[1], argv[2], argv[3])
