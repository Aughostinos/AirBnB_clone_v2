#!/usr/bin/python3
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}
class DBStorage:
    """new engine"""

    #private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')
            ), pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}

        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                #key construction
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        else:
            for cls in classes:
                objects = self.__session.query(cls).all()
                for obj in objects:
                    #key construction
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()