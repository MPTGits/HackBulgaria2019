from datetime import date
from sqlalchemy import create_engine,MetaData
from user import User
from main_database import Session, engine, Base
from patient import Patient
from doctor import Doctor
from appointment_table import AppointmentTable

Base.metadata.create_all(bind=engine)
# 3 - create a new session
session = Session()

#Users

usr1=User("Marto","fdfdsaffdssf","doctor")
usr2=User("Marto4","fdfdsaff431dssf","patoo")

#Doctors

doc1=Doctor("Meno",20,"Prof")
doc2=Doctor("Marko",18,"Assistant")

#Patients
pat1=Patient("Me4332o",20)
pat2=Patient("MarkoPatient",18)

#Tables

table_test=AppointmentTable(date(2013, 8, 23))

usr1.doctor=[doc1]
usr2.patient=[pat1]

table_test.patient=[pat1]
table_test.doctor=[doc1]

session.add(usr1)
session.add(usr2)
session.add(doc1)
session.add(pat1)
session.add(table_test)

session.commit()
session.close()


