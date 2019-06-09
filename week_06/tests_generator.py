import unittest 
import collections
from generators import *

class TestGenerators(unittest.TestCase):
#Tests for the chain funciton
    def test_concatenation_of_two_iterables_into_a_new_one_with_over_covering_values(self):
        result=chain(range(0,4),range(2,8))
        expected_output=[0,1,2,3,2,3,4,5,6,7]
        for x in expected_output:
            self.assertEqual(next(result),x)

    def test_concatenation_of_two_iterables_into_a_new_one_with_one_iterable_being_empty_list(self):
        result=chain(range(0,4),[])
        expected_output=[0,1,2,3]
        for x in expected_output:
            self.assertEqual(next(result),x)

    def test_concatenation_of_two_iterables_into_a_new_one_with_both_of_the_iterables_being_strings(self):
        result=chain("Hack ","Bulgaria")
        expected_output="Hack Bulgaria"
        for x in expected_output:
            self.assertEqual(next(result),x)




if __name__=="__main__":
    unittest.main()