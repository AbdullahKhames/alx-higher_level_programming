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


def retrieveStates(userName, pwd, dbName, searched):
    """
    retrieve States
    """
    session = getSession(userName, pwd, dbName)
    state = session.query(State)\
                   .filter(State.name == stripSearchedStr(searched))\
                   .order_by(State.id).first()
    if state is None:
        print('Not found')
    else:
        print(f"{state.id}")


def stripSearchedStr(searched):
    return searched.split(';')[0]


if __name__ == '__main__':
    """
    retrieve States
    """
    retrieveStates(argv[1], argv[2], argv[3], argv[4])
