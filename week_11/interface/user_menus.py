import sys
from datetime import date
from hospital.main_database import *
from utils.exceptions import *
from utils.constant_variables import DatabaseConstants
from hospital.user import User
from hospital.appointment_table import AppointmentTable 
from hospital.doctor import Doctor
from hospital.patient import Patient

# engine = create_engine('sqlite:////home/martogod/Python_Formal/week_11/database/'+DatabaseConstants.MAIN_DATABASE_NAME)
#     #home/martogod/101_Python_Formal/week_11/database/main_database.db')  
# #his means that all modifications tracked by Sessions (Units of Works) will be applied to the underlying database together, or none of them will.
# # In other words, Sessions are used to guarantee the database consistency.
# Session = sessionmaker(bind=engine)

# session = Session();


class PatientMenu:

    def __init__(self,patient):
        self.patient=patient

    def display_menu(self):
        print(""" Welcome to the patinet menu """ + self.patient.name + """:
                  Please select and option:
                  1.Check appointments
                  2.Check personal information
                  3.Add appointment
                  4.Remove appointment
                  5.exit\n
                """)
        option_selected=input()

        if option_selected=="1":
            q = session.query(Doctor,AppointmentTable,Patient).filter(self.patient.id == AppointmentTable.patient_id).all()
            for x in range(len(q)):
                if(q[x][2].id==self.patient.id):
                    print("Doctor:",q[x][0].title,".",q[x][0].name,"|| Date:",q[x][1].date,"|| Patient(you):",q[x][2].name)

        elif option_selected=="2":
            user_beloning_to_patient = (session.query(User,Patient).filter(self.patient.user_id ==User.id).all())
            print("Name:",self.patient.name,
                "||Age:",self.patient.age,
                "||Username for login:",user_beloning_to_patient[0][0].username)

        elif option_selected=="3":
            doctors=session.query(Doctor).all()
            print("Avaliable doctors:")
            for doctor in doctors:
                print("ID:",doctor.id,"\nDoctor name:",doctor.title,".",doctor.name,"\nAge:",doctor.age,"\n||||||||||\n")
            doctor_id=input("Enter doctor id:")
            year,month,day=input("Enter date of appointment(year/month/day):").split()
            check_doctor_id = (session.query(Doctor).filter(doctor_id==Doctor.id).all())
            if check_doctor_id==[]:
                print("Invalid doctor id")
                return
            appointment_arragment=AppointmentTable(date(int(year),int(month),int(day)))
            appointment_arragment.doctor_id=doctor_id
            appointment_arragment.patient_id=self.patient.id

            session.add(appointment_arragment)
            session.commit()

        elif option_selected=="4":
            removing_id=input("Enter appointment id to be removed:")
            q=session.query(AppointmentTable).filter(AppointmentTable.id==removing_id).all()
            session.delete(q[0])
            session.commit()

        elif option_selected=="5":
            sys.exit(0)

