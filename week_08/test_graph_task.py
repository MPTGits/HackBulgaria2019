import unittest
from graph_tasks import deep_find_DFS,DFS_visit

test_dict = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
            2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
                                                                    {'test':[{'test_key':23,
                                                                            '  something':12},
                                                                            {'good_stuff':11},
                                                                            12]}}}

class TestDFSandBFS(unittest.TestCase):

    def test_when_we_search_for_a_value_that_is_on_the_first_level_we_want_key_1_to_return_a_persons_information(self):
        expected_output={'name': 'John', 'age': '27', 'sex': 'Male'}
        searched_key=1
        self.assertEqual(deep_find_DFS(test_dict,searched_key),str(expected_output))

    def test_when_we_search_for_a_key_that_is_nested_for_example_addon_key_should_return_dict(self):
        expected_output={'test':[{'test_key':23,'something':12},{'good_stuff':11},12]}
        searched_key='addon'
        self.assertEqual(deep_find_DFS(test_dict,searched_key),str(expected_output))

if __name__=='__main__':
    unittest.main()