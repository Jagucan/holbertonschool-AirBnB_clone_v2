#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base if os.getenv('HBNB_TYPE_STORAGE') == 'db' else object):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            """Returns the list of Review instances"""
            rev_list = []
            all_revs = storage.all(Review)
            for review in all_revs.values():
                if review.place_id == self.id:
                    rev_list.append(review)
            return rev_list

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, object=None):
            ''' handles append method for adding an Amenity.id
              to the attribute amenity_ids. '''
            from models.amenity import Amenity
            if type(object) is Amenity and object.id not in self.amenity_ids:
                self.amenity_ids.append(object.id)
