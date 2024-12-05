from typing import List

def read_and_parse_from_file(file_name: str) -> List[List[int]]:
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        page_rules = []
        pages_list = []
        for line in lines:
            if line == "":
                continue
            if "|" in line:
                first, second = line.strip().split('|')
                page_rules.append(f"{second}|{first}")
            elif "," in line:
                pages_list.append(line.strip())
            
        return [page_rules, pages_list]


page_rules, pages_list = read_and_parse_from_file(file_name="./day_5/real_data.txt")
invalid_pages_list = []
for p in pages_list:
    valid = True
    pages = p.split(",")
    for x, page in enumerate(pages):
        for next_page in pages[x+1:]: 
            failing_rule = f"{page}|{next_page}"
            if failing_rule in page_rules:
                valid = False
                break
    if not valid:
        invalid_pages_list.append(pages)

all_valid = False
corrected_list = []
while not all_valid:
    all_valid = True
    for pages in invalid_pages_list:
        for x, page in enumerate(pages):
            for next_page in pages[x+1:]:
                failing_rule = f"{page}|{next_page}"
                if failing_rule in page_rules:
                    next_page_at = pages.index(next_page)
                    pages[x] = next_page
                    pages[next_page_at] = page
                    break
    
    for pages in invalid_pages_list:
        for x, page in enumerate(pages):
            for next_page in pages[x+1:]: 
                failing_rule = f"{page}|{next_page}"
                if failing_rule in page_rules:
                    valid = False
                    all_valid = False
                    break
        if valid:
            corrected_list.append(pages)
                

page_sum = 0
for pages in invalid_pages_list:
    middle_page = pages[int((len(pages) - 1)/2)]
    page_sum += int(middle_page)

print(page_sum)
