#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.city import City
import os


class State(BaseModel, Base if os.getenv('HBNB_TYPE_STORAGE') == 'db'
            else object):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            from models import storage
            """getter method that retrieves a list of City instances"""
            cities_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
