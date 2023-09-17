#!/usr/bin/python3


"""
module to define city
"""
from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base, State


class City(Base):
    __tablename__ = 'cities'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(INTEGER, ForeignKey("states.id"), nullable=False,)
    state = relationship("State", backref="cities")
