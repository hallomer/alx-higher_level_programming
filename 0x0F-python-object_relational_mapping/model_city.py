#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    City class inherits from Base,
    links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        """
        String representation of a City object.
        """
        return "<City(id='{}', name='{}', state_id='{}')>".format(
            self.id, self.name, self.state_id)
