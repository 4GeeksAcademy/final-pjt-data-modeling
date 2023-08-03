import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    dob = Column(String(250), nullable=False)

class Doctor(Base):
    __tablename__ = 'doctor'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    specialty = Column(String(250), nullable=False)
    price = Column(String(250), nullable=False)

class Appointment(Base):
    __tablename__ = 'appointment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    date = Column(String(250))
    time = Column(String(250))
    user_comment = Column(String(250), nullable=False)
   
    user = relationship(User)
    doctor = relationship(Doctor)
    def to_dict(self):
        return {}

class Report(Base):
    __tablename__ = 'report'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id'))
    date = Column(String(250))
    time = Column(String(250))
    doctor_comment = Column(String(250), nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    blood_pressure = Column(String(250))
    vo2_max = Column(Integer)
    cholesterol = Column(Integer)
   
    appointment = relationship(Appointment)
   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
