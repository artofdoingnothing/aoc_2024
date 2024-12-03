from typing import List
import re

do_not_pattern = re.compile(r"don\'t\(\)")
do_pattern = re.compile(r'do\(\)')
multiplier_pattern = re.compile(r'mul\(\d+,\d+\)') 

def read_and_parse_from_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        enabled_multipliers = []
        # This took me a while and I realized why I never really liked regex
        multiplier_list = re.split(r'([a-z]+\(\d+,\d+\))', ''.join(lines))
        enabled = True
        for multiplier in multiplier_list:
            if do_pattern.findall(multiplier): 
                enabled = True
            elif do_not_pattern.findall(multiplier): 
                enabled = False 
            elif multiplier_pattern.findall(multiplier): 
                if enabled:
                    multiplier_matches = multiplier_pattern.findall(multiplier)
                    enabled_multipliers += multiplier_matches
            
        return enabled_multipliers
    
multipliers = read_and_parse_from_file('./day_3/real_data.txt')
sum = 0
for multiplier in multipliers:
    numbers = re.findall(r'\d+', multiplier)
    numbers = list(map(int, numbers))
    sum += numbers[0] * numbers[1]
    
print(sum)
