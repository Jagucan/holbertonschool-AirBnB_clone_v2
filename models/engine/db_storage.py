#!/usr/bin/python3
"""Engine DBStorage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, session
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorge Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Crate Engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, password,
                                             host, database),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """query on the current database session all objects """
        value = {}
        if cls:
            for obj in self.__session.query(cls):
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                value[key] = obj
        else:
            for cls in [Amenity, City, Place, Review, State, User]:
                for obj in self.__session.query(cls):
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    value[key] = obj
        return value

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit the object to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the object to the current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def close(self):
        self.__session.close()