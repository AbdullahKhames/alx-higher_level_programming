#!/usr/bin/python3
"""
module to describe state model
"""
from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """
    describing the domain model
    """
    __tablename__ = 'states'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    engine = create_engine('mysql://root:1395760@localhost:3306/hbtn_0e_6_usa')
    Base.metadata.create_all(engine)
