import re

def parse_file():
    with open('./day_13/real_data.txt', 'r') as reader:
        prize_info = []
        machine_data = reader.read()
        lines = machine_data.strip().split("\n")
        
        for i in range(0, len(lines), 4):
            a_match = re.match(r"Button A: X\+([\d]+), Y\+([\d]+)", lines[i])
            b_match = re.match(r"Button B: X\+([\d]+), Y\+([\d]+)", lines[i+1])
            prize_match = re.match(r"Prize: X=([\d]+), Y=([\d]+)", lines[i+2])

            a_config = (int(a_match.group(1)), int(a_match.group(2)))
            b_config = (int(b_match.group(1)), int(b_match.group(2)))
            prize_position = (int(prize_match.group(1)) + 10000000000000, int(prize_match.group(2)) + 10000000000000)
        
            prize_info.append((a_config, b_config, prize_position))

        return prize_info

prize_info = parse_file()
tokens = 0
for a_config, b_config, prize_position in prize_info:
    x1, y1 = a_config
    x2, y2 = b_config

    a_moves = (prize_position[0]*y2 - prize_position[1]*x2) / (x1*y2 - y1*x2)
    b_moves = (prize_position[1]*x1 - prize_position[0]*y1) / (x1*y2 - y1*x2)
    if a_moves == int(a_moves) and b_moves == int(b_moves):
        tokens += int(3 * a_moves + b_moves)
    
print(tokens)

