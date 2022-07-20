import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class StarWars(Base):
    __tablename__ = 'star_wars_database'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    users_email = Column(String(250), nullable=False)
    users_password = Column(String(100), nullable=False)
    login_status = Column(String(250), nullable=False)
    star_wars_id = Column(Integer, ForeignKey('star_wars_database.id'))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    user_first_name = Column(String(100), nullable=False)
    user_lastname = Column(String(100), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    favourites_id = Column(Integer, ForeignKey('favourites.id'))

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_fav_character_id = Column(Integer, ForeignKey('character.id'))
    user_fav_planet_id = Column(Integer, ForeignKey('planet.id'))
    user_fav_vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

class UserFav(Base):
    __tablename__ = 'user_fav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_number = Column(String(250))
    character_name = Column(String(250))
    star_wars_id = Column(Integer, ForeignKey('star_wars_database.id'))
    star_wars_database = relationship(StarWars)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_description = Column(String(1000))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_number = Column(String(250))
    planet_name = Column(String(250))
    star_wars_id = Column(Integer, ForeignKey('star_wars_database.id'))
    star_wars_database = relationship(StarWars)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_description = Column(String(1000))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_number = Column(String(250))
    vehicle_name = Column(String(250))
    star_wars_id = Column(Integer, ForeignKey('star_wars_database.id'))
    star_wars_database = relationship(StarWars)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250))
    vehicle_description = Column(String(1000))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')