import unittest 
import PolynomialsandDerivates

class testPolynomialsDerivates(unittest.TestCase):
    def test_whether_a_single_variable_2_multiplyed_by_x_derived_is_displayed_correctly(self):
        single_var=PolynomialsandDerivates.SingleVariable('2*x')
        expected_result='2'
        self.assertEqual(single_var.variable_derive(),expected_result)
    def test_whether_a_single_variable_2_multi_by_x_pow_3_derived_is_displayed_correctly(self):
        single_var=PolynomialsandDerivates.SingleVariable('2*x^3')
        expected_result='6*x^2'
        self.assertEqual(single_var.variable_derive(),expected_result)
    def test_whether_a_polynom_of_a_kind_2_multy_by_x_plus_3_multi_by_x_exponent_2_plus_5(self):
        polynom=PolynomialsandDerivates.Polynom('2*x+3*x^2+5')
        expected_result='2+6*x'
        self.assertEqual(polynom.polynom_derive(),expected_result)
    def test_whether_a_polynom_of_a_kind_4_multy_by_x_exponent_3_plus_2_multi_by_x_exponent_4_plus_5(self):
        polynom=PolynomialsandDerivates.Polynom('4*x^3+2*x^4+5')
        expected_result='12*x^2+8*x^3'
        self.assertEqual(polynom.polynom_derive(),expected_result)
    def test_whether_a_single_variable_x_derived_is_displayed_correctly(self):
        polynom=PolynomialsandDerivates.Polynom('x')
        expected_result='1'
        self.assertEqual(polynom.polynom_derive(),expected_result)
    def test_whether_a_single_variable_4_derived_is_displayed_correctly(self):
        polynom=PolynomialsandDerivates.Polynom('4')
        expected_result='0'
        self.assertEqual(polynom.polynom_derive(),expected_result)
if __name__=='__main__':
    unittest.main()