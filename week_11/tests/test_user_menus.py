import unittest
import sys
sys.path.append('../interface')
from user_menus import *
sys.path.append('../hospital')
from user import User
from doctor import Doctor
from patient import Patient
from appointment_table import AppointmentTable

class TestingUserMenus(unittest.TestCase):

    #def test_if_patient_user_is_assinged_to_his_menu_bar(self):
        #user=Patient("Marto",20)
        #patient_menu=PatientMenu(user)
        #assertRaises()
