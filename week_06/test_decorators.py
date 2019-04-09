import unittest 
import decorators

class DecoratorsTests(unittest.TestCase):
    def test_when_given_name_and_integer_variables_and_correct_types_str_and_int_will_it_return_the_function_purpouse_(self):
        #deposit is a function that returns the name of the person and the deposited amount of money
        input_data=decorators.deposit("Roza", 10)
        expected_output=True
        self.assertEqual(input_data,True)
    
    def test_when_given_int_variables_and_str__type_will_it_throw_TypeError(self):
        self.assertRaises(TypeError,lambda:decorators.say_hello(2))

if __name__=='__main__':
    unittest.main()