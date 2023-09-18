#!/usr/bin/python3
"""
module to define city
"""
from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    document city class
    """
    __tablename__ = 'cities'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(INTEGER, ForeignKey("states.id"), nullable=False,)
    state = relationship("State", back_populates="cities")


if __name__ == '__main__':
    pass
