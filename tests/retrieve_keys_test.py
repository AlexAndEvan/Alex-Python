import unittest
import sys
import os
sys.path += ['..', '../..']
from AlexPython.mylib.retrieve_keys import RetrieveKeysSolver

class TestRetrieveKeys(unittest.TestCase):
    def test_init(self):
        people_locations = [20,100]
        key_locations = [60, 10, 40, 80]
        office_location = 50
        RetrieveKeysSolver.init_data_from_input(people_locations, key_locations, office_location)
        self.assertEqual(RetrieveKeysSolver.num_of_people, 2)
        self.assertEqual(RetrieveKeysSolver.num_of_keys, 4)
        print(RetrieveKeysSolver.person_key_distance)
        print(RetrieveKeysSolver.distance_list)

    def test_find_a_person_key_match_no_greater_than(self):
        people_locations = [20,100]
        key_locations = [60, 10, 40, 80]
        office_location = 50
        RetrieveKeysSolver.init_data_from_input(people_locations, key_locations, office_location)
        keys_tracking_array = [False] * RetrieveKeysSolver.num_of_keys
        a = RetrieveKeysSolver.find_a_person_key_match_no_greater_than(100, keys_tracking_array, 0)
        self.assertEqual(a, True)
        keys_tracking_array = [False] * RetrieveKeysSolver.num_of_keys
        a = RetrieveKeysSolver.find_a_person_key_match_no_greater_than(60, keys_tracking_array, 0)
        self.assertEqual(a, True)  
        keys_tracking_array = [False] * RetrieveKeysSolver.num_of_keys
        a = RetrieveKeysSolver.find_a_person_key_match_no_greater_than(50, keys_tracking_array, 0)
        self.assertEqual(a, True) 
        keys_tracking_array = [False] * RetrieveKeysSolver.num_of_keys
        a = RetrieveKeysSolver.find_a_person_key_match_no_greater_than(45, keys_tracking_array, 0)
        self.assertEqual(a, False)

    def test_find_shortest_time(self):
        people_locations = [20,100]
        key_locations = [60, 10, 40, 80]
        office_location = 50
        min_time = RetrieveKeysSolver.find_shortest_time(people_locations, key_locations, office_location)
        self.assertEqual(min_time,  50)
        
        people_locations = [11]
        key_locations = [15, 7]
        office_location = 10
        min_time = RetrieveKeysSolver.find_shortest_time(people_locations, key_locations, office_location)
        self.assertEqual(min_time,  7)
if __name__ == '__main__':
    unittest.main()