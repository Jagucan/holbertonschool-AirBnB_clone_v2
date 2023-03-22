#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """A place to stay"""
    from models import storage
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if type(storage).__name__ == "DBStorage":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")

    else:
        @property
        def rev(self):
            from models import storage
            rev_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    rev_list.append(review)
            return rev_list
