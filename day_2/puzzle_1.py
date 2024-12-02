from typing import List

def read_and_parse_from_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        reports = []
        for line in lines:
            reports.append([int(i) for i in line.strip().split()])
        return reports
    
reports = read_and_parse_from_file('./day_2/real_data.txt')

valid_reports = 0
for report in reports:
    is_increasing = False
    is_decreasing = False
    valid_report = True
    for index, level in enumerate(report):
        if index == 0:
            continue
        difference = level - report[index - 1]
        if difference >  0:
            is_increasing = True
        elif difference < 0:
            is_decreasing = True
        elif difference == 0:
            valid_report = False
            break
        
        if abs(difference) > 3:
            valid_report = False
            break
        
        if is_decreasing and is_increasing:
            valid_report = False
            break
    if valid_report:
        valid_reports += 1

print(valid_reports)
