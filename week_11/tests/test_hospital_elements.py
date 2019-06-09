import unittest
import sys
sys.path.append('../hospital')
from user import User
from doctor import Doctor
from patient import Patient
from appointment_table import AppointmentTable

class TestingHospitalModuls(unittest.TestCase):

    def test_if_user_object_is_created_with_the_correct_parameters(self):
        user=User("Marto","fwefewfs:eqwedsd","doctor")

        self.assertEqual("Marto",user.username)
        self.assertEqual("fwefewfs:eqwedsd",user.hashed_password)
        self.assertEqual("doctor",user.status)

    def test_if_Patient_object_is_created_with_the_correct_parameters(self):
        user=Patient("Marto",20)

        self.assertEqual("Marto",user.name)
        self.assertEqual(20,user.age)


    def test_if_Doctor_object_is_created_with_the_correct_parameters(self):
        user=Doctor("Marto",20,"Prof")

        self.assertEqual("Marto",user.name)
        self.assertEqual(20,user.age)
        self.assertEqual("Prof",user.title)


if __name__=='__main__':
    unittest.main()