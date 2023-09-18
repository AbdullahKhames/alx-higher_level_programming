#!/usr/bin/python3
"""
module to describe state model
"""
from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()


class State(Base):
    """
    describing the domain model
    """
    from relationship_city import City
    __tablename__ = 'states'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates='state',
                          cascade="all, delete, delete-orphan")


if __name__ == '__main__':
    pass
