with open("./day_10/real_data.txt") as reader:
    lines = reader.readlines()
    grid = []
    for line in lines:
        grid.append([int(number) for number in line.strip()])
    num_rows = len(grid)
    num_cols = len(grid[0])


def traverse_grid(row, col):
    all_possible_directions_exhausted = False
    possible_directions = [(-1, 0),(0, 1), (1, 0), (0, -1)]
    possible_trails = []
    possible_trails.append((row, col))
    highest_point_reached = 0
    while not all_possible_directions_exhausted:
        all_possible_directions_exhausted = True
        next_possible_trails = []
        for current_postion in possible_trails:
            row, col = current_postion
            if grid[row][col] == 9:
                highest_point_reached += 1
                continue
            for direction in possible_directions:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if 0 <= next_row < num_rows and 0 <= next_col < num_cols:                    
                    if grid[next_row][next_col] == grid[row][col] + 1:
                        all_possible_directions_exhausted = False
                        next_possible_trails.append((next_row, next_col))
        possible_trails = next_possible_trails
    return highest_point_reached

sum = 0

for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] == 0:
            sum += traverse_grid(row, col)
    
print(sum)

