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
    region_info = {"area": 0, "sides": 0}
    stack = [(row, col)]
    region = set()

    while stack:
        row, col = stack.pop()
        if (row, col) in visited_cells:
            continue

        visited_cells.add((row, col))
        region.add((row, col))
        region_info["area"] += 1

        for direction in possible_neighbors:
            next_row = row + direction[0]
            next_col = col + direction[1]
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                if map_grid[next_row][next_col] == plant:
                    if (next_row, next_col) not in visited_cells:
                        stack.append((next_row, next_col))

    
    boundary_objects = set()
    for x, y in region:
        for dx, dy in possible_neighbors:
           new_x, new_y = x + dx, y + dy 
           if (new_x, new_y) not in region:
                boundary_objects.add(((new_x, new_y), (dx, dy)))

    sides = 0
    while len(boundary_objects) > 0:
        (x, y), (dx, dy) = boundary_objects.pop()
        sides += 1
        
        next_x, next_y = x + dy, y - dx
        while ((next_x, next_y), (dx, dy)) in boundary_objects: 
            boundary_objects.remove(((next_x, next_y), (dx, dy)))
            next_x, next_y = next_x + dy, next_y - dx

        next_x, next_y = x - dy, y + dx
        while ((next_x, next_y), (dx, dy)) in boundary_objects: 
            boundary_objects.remove(((next_x, next_y), (dx, dy)))
            next_x, next_y = next_x - dy, next_y + dx
    
    region_info["sides"] = sides
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
        fence_price += region["area"] * region["sides"]

print(fence_price)
