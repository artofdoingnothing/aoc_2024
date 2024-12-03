from typing import List
import re

def read_and_parse_from_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        multipliers = []
        pattern = re.compile(r'mul\(\d+,\d+\)')
        line = ''.join(lines)
        matches = pattern.findall(line)
        multipliers += matches
        return multipliers
    
multipliers = read_and_parse_from_file('./day_3/real_data.txt')
sum = 0

for multiplier in multipliers:
    numbers = re.findall(r'\d+', multiplier)
    numbers = list(map(int, numbers))
    sum += numbers[0] * numbers[1]
    
print(sum)
