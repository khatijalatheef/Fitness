from sqlalchemy import Column, Integer, String, DateTime
from database import Base  # <-- import the Base from database.py

class FitnessClass(Base):  # <-- use imported Base here
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    datetime = Column(DateTime)
    instructor = Column(String)
    slots = Column(Integer)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer)
    client_name = Column(String)
    client_email = Column(String)
