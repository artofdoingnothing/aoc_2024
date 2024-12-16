import re
from collections import defaultdict


robots = []
with open("day_14/real_data.txt", "r") as f:
    for line in f:
        match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        if match:
            col, row, col_diff, row_diff = map(int, match.groups())
            robots.append(((row, col), (row_diff, col_diff)))
width = 101
height = 103
time = 100
grid = defaultdict(int)
for (row, col), (row_diff, col_diff) in robots:
    new_x = (row + row_diff * time) % height
    new_y = (col + col_diff * time) % width
    grid[(new_x, new_y)] += 1

quadrant1_count = 0
quadrant2_count = 0
quadrant3_count = 0
quadrant4_count = 0

mid_row = height // 2
mid_col = width // 2


for (x,y), count in grid.items():
    if x < mid_row and y < mid_col:
        quadrant1_count += count
    elif x > mid_row and y < mid_col:
       quadrant2_count += count
    elif x < mid_row and y > mid_col:
     quadrant3_count += count
    elif x > mid_row and y > mid_col:
        quadrant4_count += count

print(quadrant1_count * quadrant2_count * quadrant3_count * quadrant4_count)
