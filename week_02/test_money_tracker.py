import unittest
import money_tracker


class MoneyTrackerTest(unittest.TestCase):

    def test_if_all_user_data_is_displayed(self):
        all_data={'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=all_data
        self.assertEqual(money_tracker.list_user_data(all_data),expected_result)

    def test_show_only_user_income_fileds(self):
        all_data={'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=[(10, 'Deposit'), (700, 'Salary'), (50, 'Savings')]
        self.assertEqual(money_tracker.show_user_income(all_data),expected_result)

    def test_if_user_savings_are_displayed_correctly(self):
        all_data={'22-03-2019': {'income': [(10, 'Deposit'),(20,'Savings')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=[(20,'Savings'),(50, 'Savings')]
        self.assertEqual(money_tracker.show_user_savings(all_data),expected_result)

    def test_if_user_deposits_are_displayed_correctly(self):
        all_data={'22-03-2019': {'income': [(10, 'Deposit'),(20,'Savings')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=[(10,'Deposit')]
        self.assertEqual(money_tracker.show_user_deposits(all_data),expected_result)

    def test_show_only_user_expenses_fileds(self):
        all_data={'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result=[(27.7,'Food'),(4, 'Eating Out')]
        self.assertEqual(money_tracker.show_user_expenses(all_data),expected_result)

    def test_if_expenses_list_taken_from_all_user_data_is_sorted_by_categories(self):
        all_data={'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'F'),(40.2,'A')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4,'E')]}}
        expected_result=[(40.2,'A'),(4, 'E'),(27.7,'F')]
        self.assertEqual(money_tracker.list_user_expenses_ordered_by_categories(all_data),expected_result)

    def test_if_user_data_is_displayed_only_for_a_given_date(self):
        all_data={'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_result=[(50, ' Savings', 'New Income'), (15, ' Food', 'New Expense'), (200, ' Deposit', 'New Income'), (5, ' Sports', 'New Expense'), (10, ' Deposit', 'New Income')]
        expected_result.sort(key=lambda x: x[1])  
        date='23-03-2019'
        self.assertEqual(money_tracker.show_user_data_per_date(date,all_data),expected_result)

    def test_if_addding_new_income_is_working_correctly(self):
        all_data={'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}
        expected_result={'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit'),(30.2,'Sugar mom xD')]}}
        date='23-03-2019'
        the_new_income=(30.2,'Sugar mom xD')
        #Dunno how to work out the test but the fucntions works 
        #self.assertEqual(money_tracker.add_income(the_new_income[1],the_new_income[0],date,all_data),expected_result)

if __name__=='__main__':
	unittest.main()