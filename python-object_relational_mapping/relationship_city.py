#!/usr/bin/python3
"""
This module defines the City class for SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class that represents the cities table in the database
    
    Attributes:
        id: Primary key, auto-generated integer
        name: City name, string up to 128 characters, cannot be null
        state_id: Foreign key referencing states.id, cannot be null
    """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
