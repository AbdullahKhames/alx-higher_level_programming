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


def updateState(userName, pwd, dbName):
    """
    update State
    """
    session = getSession(userName, pwd, dbName)
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()


if __name__ == '__main__':
    """
    retrieve States
    """
    updateState(argv[1], argv[2], argv[3])
