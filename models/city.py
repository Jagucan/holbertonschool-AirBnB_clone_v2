#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base if os.getenv('HBNB_TYPE_STORAGE') == 'db' else object):
    """ The city class, contains state ID and name """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

        places = relationship("Place", backref="city",
                              cascade="all, delete, delete-orphan",)
