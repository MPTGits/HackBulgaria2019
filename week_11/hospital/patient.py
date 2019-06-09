from sqlalchemy import Column, String, Integer, Date,ForeignKey
from sqlalchemy.orm import relationship, backref
from hospital.main_database import Base


class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    #appointments_table_id=Column(Integer,ForeignKey('AppointmentTable.id'))
    #apointments_table=relationship("AppointmentTable",uselist=True,backref="patient")
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship("User",backref="patient")


    def __init__(self, name, age):
        self.name= name
        self.age=age
