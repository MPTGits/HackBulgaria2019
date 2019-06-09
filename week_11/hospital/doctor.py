
from sqlalchemy import Column, String, Integer, Date,ForeignKey
from sqlalchemy.orm import relationship, backref
from hospital.main_database import Base

class Doctor(Base):
    __tablename__ = 'doctor'

    title=Column(String)
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship("User",backref="doctor")

    def __init__(self, name, age,title):
        self.name= name
        self.age=age
        self.title=title
