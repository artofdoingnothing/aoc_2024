from collections import deque

with open("./day_9/real_data.txt") as reader:
    file_info_input = reader.readline().strip()

free_locations = []
current_id = 0
disk_info_list = []
disk_length = 0

for idx, f in enumerate(file_info_input):
    if idx % 2 == 0:
        for i in range(int(f)):
            disk_info_list.append(current_id)
            disk_length += 1
        current_id += 1
    else:
        for i in range(int(f)):
            disk_info_list.append('.')
            free_locations.append(disk_length)
            disk_length += 1

free = deque(free_locations)
all_consolidated = False

while True:
    current_free_spot = free.popleft()
    for idx, ele in enumerate(disk_info_list[::-1]):
        if not ele == ".":
            shiftable_file = ele
            shiftable_file_index = len(disk_info_list) - idx - 1
            if '.' not in disk_info_list[:shiftable_file_index+1]:
                all_consolidated = True
            break
    if all_consolidated:
        break
    disk_info_list[shiftable_file_index] = '.'
    disk_info_list[current_free_spot] = shiftable_file

sum = 0
for idx, file in enumerate(disk_info_list):
    if not file == ".": 
        sum += idx * file

print(sum) 
