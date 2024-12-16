import re
from collections import defaultdict
from operator import itemgetter
from itertools import groupby


robots = []
with open("day_14/real_data.txt", "r") as f:
    for line in f:
        match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        if match:
            col, row, col_diff, row_diff = map(int, match.groups())
            robots.append(((row, col), (row_diff, col_diff)))
width = 101
height = 103
time = 0
tree_base_detected = False
grid = defaultdict(int)

def find_longest_consecutive_sublist(arr):
    if not arr:
        return []
    
    arr.sort()

    max_sublist = []
    current_sublist = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_sublist.append(arr[i])
        else:
            if len(current_sublist) > len(max_sublist):
                max_sublist = current_sublist
            current_sublist = [arr[i]]

    if len(current_sublist) > len(max_sublist):
        max_sublist = current_sublist

    return max_sublist

while not tree_base_detected:
    grid = defaultdict(int)
    time+=1
    for (row, col), (row_diff, col_diff) in robots:
        new_x = (row + row_diff * time) % height
        new_y = (col + col_diff * time) % width
        grid[(new_x, new_y)] += 1
    
    sorted_robot_locations = sorted(grid.keys(), key=itemgetter(0))
    robot_locations_by_row = [ (k,list(v)) for k,v in groupby(sorted_robot_locations, key=itemgetter(0))]

    for idx, row in enumerate(robot_locations_by_row):
        _, robot_cell_list = row
        col_list = find_longest_consecutive_sublist([r[1] for r in robot_cell_list])
        if len(col_list) > 10 and idx > 3:
            previous_previous_col_list = find_longest_consecutive_sublist([r[1] for r in robot_locations_by_row[idx - 2][1]])
            previous_col_list = find_longest_consecutive_sublist([r[1] for r in robot_locations_by_row[idx - 1][1]])
            if  len(previous_col_list) == len(col_list) - 2 and len(previous_previous_col_list) == len(col_list) - 4:
                tree_base_detected = True
                break

for row in range(height):
    for col in range(width):
        if (row,col) in grid.keys():
            print("+", end='')
        else:
            print(".", end='')
    print("")
print(time)
    



