
class RetrieveKeysSolver:
    num_of_people = 0
    num_of_keys = 0
    person_key_distance = [0]
    distance_list = [0]

    @staticmethod
    def retrieve_keys():
        return 1

    @staticmethod
    def init_data_from_input(people_locations, key_locations, office_location):
        RetrieveKeysSolver.num_of_people = len(people_locations)
        RetrieveKeysSolver.num_of_keys = len(key_locations)
        RetrieveKeysSolver.person_key_distance = [[0] * RetrieveKeysSolver.num_of_keys for i in range(RetrieveKeysSolver.num_of_people)]
        distance_set = set()
        for i in range(RetrieveKeysSolver.num_of_people):
            for j in range(RetrieveKeysSolver.num_of_keys):
                person_location = people_locations[i]
                key_location = key_locations[j]
                if(person_location > office_location):
                    distance = person_location - office_location
                    if(key_location > person_location):
                        distance += (key_location - person_location) * 2
                    elif(key_location < office_location):
                            distance += (office_location - key_location) * 2
                if(person_location < office_location):
                    distance = office_location - person_location
                    if(key_location < person_location):
                        distance += (person_location - key_location) * 2
                    elif(key_location > office_location):
                            distance += (key_location - office_location) * 2   
                RetrieveKeysSolver.person_key_distance[i][j] = distance
                distance_set.add(distance)
        RetrieveKeysSolver.distance_list = list(distance_set)
        RetrieveKeysSolver.distance_list.sort()
    
    @staticmethod
    def find_shortest_time(people_locations, key_locations, office_location):
        RetrieveKeysSolver.init_data_from_input(people_locations, key_locations, office_location)
        i = len(RetrieveKeysSolver.distance_list) - 1
        j = 0
        k = (i+j)//2
        min_time = RetrieveKeysSolver.distance_list[i]
        while(i >= j):
            distance = RetrieveKeysSolver.distance_list[k]
            if_has_a_match = RetrieveKeysSolver.find_a_person_key_match_no_greater_than(
                distance, 
                [False] * RetrieveKeysSolver.num_of_keys,
                0
            )
            if if_has_a_match:
                i = k-1
                min_time = distance
            else:
                j = k+1
            k = (i+j)//2
        return min_time

    @staticmethod
    def find_a_person_key_match_no_greater_than(distance, keys_tracking_array, i):
        if i == RetrieveKeysSolver.num_of_people:
            return True

        for j in range(RetrieveKeysSolver.num_of_keys):
            if(RetrieveKeysSolver.person_key_distance[i][j] > distance) or (keys_tracking_array[j]):
                continue
            keys_tracking_array[j] = True
            if RetrieveKeysSolver.find_a_person_key_match_no_greater_than(distance, keys_tracking_array, i+1):
                return True
            keys_tracking_array[j] = False
        return False