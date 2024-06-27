#!/usr/bin/python3
"""
State module
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """getter method for cities when using FileStorage"""
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values(
                ) if city.state_id == self.id]
