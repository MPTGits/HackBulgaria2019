from sqlalchemy import Column, String, Integer, Date,ForeignKey
from sqlalchemy.orm import relationship, backref
from hospital.main_database import Base

class AppointmentTable(Base):
    __tablename__ = 'AppointmentTable'

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer,ForeignKey('doctor.id'))
    doctor=relationship("Doctor",uselist=True,backref="AppointmentTable")
    patient_id = Column(Integer,ForeignKey('patient.id'))
    patient=relationship("Patient",uselist=True,backref="AppointmentTable")
    date=Column(Date)


    def __init__(self, date):
        self.date=date