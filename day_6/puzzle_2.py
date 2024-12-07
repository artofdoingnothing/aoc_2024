with open("./day_6/real_data.txt") as reader:
    grid = reader.readlines()
    num_rows = len(grid)
    num_cols = len(grid[0])

for r in range(num_rows):
    for c in range(num_cols):
        if grid[r][c] == '^':
            start_row, start_col = r, c
            break
    else:
        continue
    break

moves = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

obstacles_placed = 0

for row in range(num_rows):
    for col in range(num_cols):
        current_row, current_col = start_row, start_col
        direction = "up"
        visited_cells_with_directions = set()
        
        while True:
            if (current_row, current_col, direction) in visited_cells_with_directions:
                obstacles_placed += 1
                break
            visited_cells_with_directions.add((current_row, current_col, direction))

            next_row = current_row + moves[direction][0]
            next_col = current_col + moves[direction][1]

            if not (0 <= next_row < num_rows and 0 <= next_col < num_cols):
                break

            if grid[next_row][next_col] == '#' or (next_row == row and next_col == col):
                direction = {"up": "right", "right": "down", "down": "left", "left": "up"}[direction]
            else:
                current_row, current_col = next_row, next_col

print(obstacles_placed)
