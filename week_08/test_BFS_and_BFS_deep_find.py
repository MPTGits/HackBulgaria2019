import unittest
from BFS_and_DFS_deep_find import deep_find_DFS,deep_find_BFS
from deep_find_all import deep_find_DFS_all,deep_find_BFS_all
from deep_apply import deep_apply_DFS

test_dict = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
            2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
                                                                    {'test':[{'test_key':23,
                                                                            'something':12},
                                                                            {'good_stuff':11},
                                                                            12,
                                                                            {23:12}]}},
            'test':"Found ya"}

class TestDFSandBFS(unittest.TestCase):

    def test_when_we_search_for_a_value_that_is_on_the_first_level_we_want_key_1_to_return_a_persons_information(self):
        expected_output={'name': 'John', 'age': '27', 'sex': 'Male'}
        searched_key=1
        self.assertEqual(deep_find_DFS(test_dict,searched_key),expected_output)

    def test_when_we_search_for_a_key_that_is_nested_for_example_addon_key_should_return_dict(self):
        expected_output={'test':[{'test_key':23,'something':12},{'good_stuff':11},12,{23:12}]}
        searched_key='addon'
        self.assertEqual(deep_find_DFS(test_dict,searched_key),expected_output)

    def test_for_finding_the_top_most_value_of_key_with_value_name(self):
        expected_output='John'
        searched_key='name';
        self.assertEqual(deep_find_DFS(test_dict,searched_key),expected_output)

    def test_if_given_Data_is_empty(self):
        expected_output=None
        searched_key="whatever";
        self.assertEqual(deep_find_DFS({},searched_key),expected_output);

    #Same tests but for BFS

    def test_BFS_when_we_search_for_a_value_that_is_on_the_first_level_we_want_key_1_to_return_a_persons_information(self):
        expected_output={'name': 'John', 'age': '27', 'sex': 'Male'}
        searched_key=1
        self.assertEqual(deep_find_BFS(test_dict,searched_key),expected_output)

    def test_BFS_when_we_search_for_a_key_that_is_nested_for_example_addon_key_should_return_dict(self):
        expected_output={'test':[{'test_key':23,'something':12},{'good_stuff':11},12,{23:12}]}
        searched_key='addon'
        self.assertEqual(deep_find_BFS(test_dict,searched_key),expected_output)

    def test_BFS_for_finding_the_top_most_value_of_key_with_value_name(self):
        expected_output='John'
        searched_key='name';
        self.assertEqual(deep_find_BFS(test_dict,searched_key),expected_output)

    def test__BFS_if_given_Data_is_empty(self):
        expected_output=None
        searched_key="whatever";
        self.assertEqual(deep_find_BFS({},searched_key),expected_output);

    #Testing deep find for DFS and BFS
    #DFS
    def test_DFS_deep_find_all_keys_with_value_test(self):
        values=[]
        searched_key='test';
        expected_output=[[{'test_key':23,'something':12},{'good_stuff':11},12,{23:12}],"Found ya"]
        deep_find_DFS_all(test_dict,searched_key,values)
        self.assertEqual(values,expected_output)

    def test_DFS_deep_find_all_keys_with_value_23(self):
        values=[]
        searched_key=23;
        expected_output=[12]
        deep_find_DFS_all(test_dict,searched_key,values)
        self.assertEqual(values,expected_output)
    def test_DFS_if_key_is_not_present_in_data_dict(self):
        values=[]
        searched_key='Marto';
        expected_output=[]
        deep_find_DFS_all(test_dict,searched_key,values)
        self.assertEqual(values,expected_output)
    #BFS
    def test_BFS_deep_find_all_keys_with_value_test(self):
        values=[]
        searched_key='test';
        expected_output=["Found ya",[{'test_key':23,'something':12},{'good_stuff':11},12,{23:12}]]
        deep_find_BFS_all(test_dict,searched_key,values)
        self.assertEqual(values,expected_output)

    def test_BFS_deep_find_all_keys_with_value_23(self):
        values=[]
        searched_key=23;
        expected_output=[12]
        deep_find_BFS_all(test_dict,searched_key,values)
        self.assertEqual(values,expected_output)
    def test_BFS_if_key_is_not_present_in_data_dict(self):
        values=[]
        searched_key='Marto';
        expected_output=[]
        deep_find_BFS_all(test_dict,searched_key,values)
        self.assertEqual(values,expected_output)
#Deep apply testing 
    def test_deep_apply_change_test_key_values_to_the_number_666(self):
        new_value=666
        searched_key='test'
        
        local_test_dict=test_dict = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
            2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
                                                                    {'test':[{'test_key':23,
                                                                            'something':12},
                                                                            {'good_stuff':11},
                                                                            12,
                                                                            {23:12}]}},
            'test':"Found ya"}

        expected_output={1: {'name': 'John', 'age': '27', 'sex': 'Male'},
            2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
                                                                    {'test':666}},
            'test':666}
            
        deep_apply_DFS(local_test_dict,searched_key,new_value)
        self.assertEqual(local_test_dict,expected_output)


if __name__=='__main__':
    unittest.main()