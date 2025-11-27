#!/usr/bin/python3
"""
This module defines the State class for SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    State class that represents the states table in the database
    
    Attributes:
        id: Primary key, auto-generated integer
        name: State name, string up to 128 characters, cannot be null
        cities: Relationship with City class, with cascade delete
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan"
    )
