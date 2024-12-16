with open("./day_12/real_data.txt") as reader:
    map_grid = []
    for line in reader.readlines():
        map_grid.append(line.strip())
    num_rows = len(map_grid)
    num_cols = len(map_grid[0])

possible_neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
plot_info = {}
visited_cells = set()

def explore_region(row, col, plant):
    region_info = {"area": 0, "perimeter": 0}
    stack = [(row, col)]

    while stack:
        row, col = stack.pop()
        if (row, col) in visited_cells:
            continue

        visited_cells.add((row, col))
        region_info["area"] += 1
        total_perimeter = 4

        for direction in possible_neighbors:
            next_row = row + direction[0]
            next_col = col + direction[1]
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                if map_grid[next_row][next_col] == plant:
                    total_perimeter -= 1
                    if (next_row, next_col) not in visited_cells:
                        stack.append((next_row, next_col))

        region_info["perimeter"] += total_perimeter
    return region_info


for row in range(num_rows):
    for col in range(num_cols):
        if (row, col) not in visited_cells:
            plant = map_grid[row][col]
            region_info = explore_region(row, col, plant)

            if plant not in plot_info:
                plot_info[plant] = []
            plot_info[plant].append(region_info)

fence_price = 0
for plant_regions in plot_info.values():
    for region in plant_regions:
        fence_price += region["area"] * region["perimeter"]

print(fence_price)
