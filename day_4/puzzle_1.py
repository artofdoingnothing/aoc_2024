from typing import List
import re

def get_diagonal_elements(array):
    diagonals = []
    rows = len(array)
    cols = len(array[0])

    for k in range(rows + cols - 1):
        diagonal = []
        for i in range(max(0, k - cols + 1), min(k + 1, rows)):
            j = k - i
            diagonal.append(array[i][j])
        diagonals.append(diagonal)

    return diagonals

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

def count_xmas_occurrences(text):
    pattern = r'(?=(XMAS|SAMX))'
    matches = re.findall(pattern, text)
    return len(matches)

no_of_xmases = 0

letters_list = read_and_parse_from_file(file_name="./day_4/real_data.txt")
for letters in letters_list:
    search_str = "".join(letters)
    no_of_xmases += count_xmas_occurrences(search_str)

transposed_array = [list(row) for row in list(zip(*letters_list))]
for letters in transposed_array:
    search_str = "".join(letters)
    no_of_xmases += count_xmas_occurrences(search_str)

diagonal_letters_list_from_top_left = get_diagonal_elements(letters_list)
for letters in diagonal_letters_list_from_top_left:
    search_str = "".join(letters)
    no_of_xmases += count_xmas_occurrences(search_str)

reversed_letters_list = [l[::-1] for l in letters_list ]
diagonal_letters_list_from_top_right = get_diagonal_elements(reversed_letters_list)
for letters in diagonal_letters_list_from_top_right:
    search_str = "".join(letters)
    no_of_xmases += count_xmas_occurrences(search_str)


print(no_of_xmases)
