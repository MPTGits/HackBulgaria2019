import unittest
from week2_solutions import elevator_trips
 


class testElevatorTripsFunction(unittest.TestCase):
    
    def test_when_list_of_people_weight_and_list_of_floors_to_go_isnt_bjection(self):
        people_weights=[60,80,212.4,68.7]
        floors_to_go=[2,4,5]
        elevator_floors=5
        max_people=3
        max_weight=300
        self.assertRaises(ValueError,lambda:elevator_trips(people_weights,floors_to_go,elevator_floors,max_people,max_weight))
    
    def test_when_both_of_the_lists_are_empty(self):
        self.assertRaises(ValueError,lambda:elevator_trips([], [], 5, 2, 200))

    def test_when_there_are_5_people_and_3_diffrent_floors_to_go_to(self):
        people_weights=[40, 40, 100, 80, 60]
        floors_to_go=[2, 3, 3, 2, 3]
        elevator_floors=3
        max_people=5
        max_weight=200
        expecte_output=6
        self.assertEqual(elevator_trips(people_weights, floors_to_go, elevator_floors, max_people, max_weight),expecte_output)

    def test_when_there_are_3_people_and_5_diffrent_floors_to_go_to(self):
        people_weights=[80, 60, 40]
        floors_to_go=[2, 3, 5]
        elevator_floors=5
        max_people=2
        max_weight=200
        expecte_output=5
        self.assertEqual(elevator_trips(people_weights, floors_to_go, elevator_floors, max_people, max_weight),expecte_output)



if __name__=='__main__':
    unittest.main()

