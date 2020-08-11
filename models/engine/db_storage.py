#!/usr/bin/python3
"""Engine DBStorage Module"""
from sqlalchemy import create_engine, MetaData
from os import getenv


class DBStorage:
    """New Engine
    Attributes:
        engine: set to None
        session: set to None
    """
    __engine = None
    __session = None

    def __init__(self):
        """"""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """all objects depending of the class name"""
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        clss = [User, City, State, Amenity, Place, Review]
        rows = []
        #dic = {}

        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in clss:
                rows += self.__session.query(cls)

        return {type(v).__name__ + "." + v.id: v for v in rows}

        #for v in rows.values():
        #    dic = "{}.{}".format(type(v).__name__, v.id)


    def new(self, obj):
        """add the object to the current database session"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the database"""
        from models.base_model import Base
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        sess_factory = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
