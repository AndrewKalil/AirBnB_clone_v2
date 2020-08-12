#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, relationship
from os import getenv

class Amenity(BaseModel, Base):
    """"Class that Define the Amenities"""

    __tablename__ = "amenities"
    name = Column(String(128),
                  nullable=False)

    place_amenities = relationship("Place",
                                   secondary=place_amenity)
