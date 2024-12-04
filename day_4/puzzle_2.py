from typing import List

def read_and_parse_from_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        letters_list = []
        for line in lines:
            if line == "":
                continue
            letters = [l for l in line.strip()]
            letters_list.append(letters)

        return letters_list

no_of_elements = 0
letters_list = read_and_parse_from_file(file_name="./day_4/real_data.txt")

for row, letters in enumerate(letters_list):
    for col, letter in enumerate(letters):
        if letter == 'A':
            if row == 0 or col == 0 or row == len(letters_list) - 1 or col == len(letters) - 1:
                continue
            
            right_diagonal = letters_list[row-1][col-1] + "A" + letters_list[row+1][col+1]
            if not right_diagonal == "MAS" and not right_diagonal == "SAM":
                continue

            left_diagonal = letters_list[row-1][col+1] + "A" + letters_list[row+1][col-1]
            if not left_diagonal == "MAS" and not left_diagonal == "SAM":
                continue
            
            no_of_elements += 1
             

print(no_of_elements)
