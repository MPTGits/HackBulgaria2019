import unittest
from simplify_fraction import simpl_fraction,sum_fractions,sort_fractions

class testFractionSimplifyer(unittest.TestCase):
    def test_if_given_value_is_list(self):
        list_with_a_no_tuple_value=[(1,2),2]
        self.assertRaises(ValueError, simpl_fraction,list_with_a_no_tuple_value)
    def test_if_we_have_2_and_4(self):
        tuple_frac=(2,4)
        self.assertEqual(simpl_fraction(tuple_frac),(1,2))
    def test_if_given_value_is_divison_denominator_is_zero(self):
        list_with_a_0_denominator=(1,0)
        self.assertRaises(ZeroDivisionError, simpl_fraction,list_with_a_0_denominator)
    def test_the_sum_of_2_4__1_2__1_4(self):
        tuple_frac=[(2,4),(1,2),(1,4)]
        self.assertEqual(sum_fractions(tuple_frac),(5,4))
    def test_if_list_of_fractions_is_sorted(self):
        fractions=[(3,4),(1,2),(5,2),(2,2)]
        self.assertEqual(sort_fractions(fractions),[(1,2),(3,4),(2,2),(5,2)])


if __name__=='__main__':
    unittest.main()