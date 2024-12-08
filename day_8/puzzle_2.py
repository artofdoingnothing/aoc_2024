from itertools import combinations

with open("./day_8/real_data.txt") as reader:
    grid = [line.strip() for line in reader.readlines()]
    num_rows = len(grid)
    num_cols = len(grid[0])

antenna_locations = {}
all_antena_locations = set()
antinode_locations = set()

def find_antinodes(coordinates_1, coordinates_2, multiplier):
    dxa = coordinates_2[0] - coordinates_1[0]
    dya = coordinates_2[1] - coordinates_1[1]

    dxb = coordinates_1[0] - coordinates_2[0]
    dyb = coordinates_1[1] - coordinates_2[1]

    antinode_1 = (coordinates_1[0] + multiplier * dxa), (coordinates_1[1] + multiplier * dya)
    antinode_2 = (coordinates_2[0] + multiplier * dxb), (coordinates_2[1] + multiplier * dyb)

    return antinode_1, antinode_2

def valid_antinode(antinode):
    if 0 <= antinode[0] < num_rows and 0 <= antinode[1] < num_cols:
        if not antinode in antinode_locations:
            return True

    return False 


for row in range(num_rows):
    for col in range(num_cols):
        element = grid[row][col] 
        if  element == '.':
            continue
        
        if element not in antenna_locations.keys():
            antenna_locations[element] = []
        
        antenna_locations[element].append((row, col))
        all_antena_locations.add((row, col))


for _antenna_name, antenna_coordinates in antenna_locations.items():
    for antenna_1, antenna_2 in combinations(antenna_coordinates, 2):
        for multiplier in range(2, 40, 1):
            antinode_1, antinode_2 = find_antinodes(antenna_1, antenna_2, multiplier)
            if valid_antinode(antinode_1):
                antinode_locations.add(antinode_1)
            if valid_antinode(antinode_2):
                antinode_locations.add(antinode_2)
            if valid_antinode(antenna_1):
                antinode_locations.add(antenna_1)
            if valid_antinode(antenna_2):
                antinode_locations.add(antenna_2)

print(len(antinode_locations))
