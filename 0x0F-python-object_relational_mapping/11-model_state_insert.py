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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == '__main__':
    """
    retrieve States
    """
    retrieveStates(argv[1], argv[2], argv[3])
