#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.place import place_amenity


class Amenity(BaseModel, Base if os.getenv('HBNB_TYPE_STORAGE') == 'db'
              else object):
    """Class Amenity"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
