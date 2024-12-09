from collections import deque

with open("./day_9/real_data.txt") as reader:
    file_info_input = reader.readline().strip()

disk_info_list = []
file_sizes = {}
current_id = 0

for idx, f in enumerate(file_info_input):
    if idx % 2 == 0:
        file_sizes[current_id] = int(f)
        for i in range(int(f)):
            disk_info_list.append(current_id)
        current_id += 1
    else:
        for i in range(int(f)):
            disk_info_list.append('.')

for file_id in sorted(file_sizes.keys(), reverse=True):
    file_size = file_sizes[file_id]
    first_occurrence = disk_info_list.index(file_id)
    free_space_start = -1
    free_space_count = 0
    for i in range(first_occurrence):
        if disk_info_list[i] == '.':
            if free_space_start == -1:
                free_space_start = i
            free_space_count += 1
        else:
            free_space_start = -1
            free_space_count = 0

        if free_space_count == file_size:
            for i in range(file_size):
                disk_info_list[free_space_start + i] = file_id
                disk_info_list[first_occurrence + i] = '.'
            break


sum = 0
for idx, file in enumerate(disk_info_list):
    if file != '.':
        sum += idx * file

print(sum)
