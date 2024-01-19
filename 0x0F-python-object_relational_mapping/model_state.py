#!/usr/bin/python3
"""
Import the modules
Declarative_base from thesqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


""" Creating the directive base """
Base = declarative_base()


class State(Base):
    """
     The state Class Definition
    Params:
       id: id field ogf the class
       name: state name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
