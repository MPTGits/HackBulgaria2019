import getpass
import getch
import sys
from main_controler import SigningControler
from user_menus import *
from utils.exceptions import *

class StartUpMenu:

#Function to display asteriks in our char places for password
    @staticmethod
    def __type_password():
        passwrd = ''
        typed_char = ''

        while True:
            typed_char = getch.getch()

            if typed_char == '\n':
                print(typed_char)
                break

            passwrd += typed_char

            print('*', end='', flush=True)
        #Note that white spaces will be removed
        passwrd=passwrd.replace(" ","")

        return passwrd

    @classmethod
    def run_startUp(cls):
        print(""" Welcome to the patinet/doctor register
                  Please select and option:
                  1.Sign in
                  2.Sign up
                  3.exit\n
                """)
        option_selected=input()
        
        if not (option_selected.isdigit() and 1<=int(option_selected)<=3):
            print("Sorry,invalid option selected!")
            return

        if option_selected=='3':
            sys.exit(0)

        user=input("Username:\n")
        print("Password:")
        #Note that white spaces will be removed
        password=cls.__type_password()
        
        if option_selected=='1':
            try:
                user=SigningControler.login(user,password)
            except InvalidUserData:
                print("Invalid username or password!")
                sys.exit(1)

#TODO:Implement the exceptions
        elif option_selected=='2':
            print("Confirmation password:")
            confirmation_password=cls.__type_password()
            status=input("Enter your status(patient/doctor):")
            try:
                user=SigningControler.register(user,password,confirmation_password,status)
            except ExistingUser:
                print("Username is already registered!")
                sys.exit(1)
            except InvalidUsername:
                print("Username contains none alphabetic symbols!")
                sys.exit(1)
            except UnmatchingPasswords:
                print("Entered passwords do not match!")
                sys.exit(1)
            if status=="patient":
                name=input("Input name:")
                age=input("Input age:")
                
                patient_to_be_added=Patient(name,age)
                patient_to_be_added.user_id=user.id
                
                session.add(patient_to_be_added)
                session.commit( )

        #Geting the user menu we need
        if user.status=="patient":
            logged_in_patient=session.query(Patient).filter(Patient.user_id==user.id).all()
            patient_menu=PatientMenu(logged_in_patient[0])
            while True:
                session.commit()
                patient_menu.display_menu()


StartUpMenu.run_startUp()