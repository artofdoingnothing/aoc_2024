from typing import List
import re

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


location_ids_right = location_id_list[1]
location_ids_left_list = location_id_list[0]

similarity_score = 0

for idx, location_id in enumerate(location_ids_left_list):
    if location_id in location_ids_right:
        matches = [lr_id for lr_id in location_ids_right if lr_id == location_id]
        similarity_score += location_id * len(matches)

print(similarity_score)
