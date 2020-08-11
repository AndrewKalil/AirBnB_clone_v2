#!/usr/bin/python3
"""Engine DBStorage Module"""
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State

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

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects depending of the class name"""
        clss = [City,
                State]
        objs = []
        _dic = {}

        if cls:
            objs = self.__session.query(cls).all()
        else:
            for cls in clss:
                objs += self.__session.query(cls)

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, str(obj.id))
            _dic[key] = obj

        return _dic


    def new(self, obj):
        """add the object to the current database session"""
        if obj:
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
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)

        sess_factory = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
