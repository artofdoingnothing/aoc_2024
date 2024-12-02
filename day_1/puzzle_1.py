from typing import List

def read_and_parse_from_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        location_list = [[] for _ in lines[0].strip().split()]
        for line in lines:
            location_ids = line.split()
            for location_index, location_id in enumerate(location_ids):
                location_list[location_index].append(int(location_id))

        return location_list


location_id_list = read_and_parse_from_file(file_name="./day_1/real_data.txt")
for llist in location_id_list:
    llist.sort()
distance = 0
for index, _ in enumerate(location_id_list[0]):
    distance += abs(location_id_list[0][index] - location_id_list[1][index])

print(distance)
