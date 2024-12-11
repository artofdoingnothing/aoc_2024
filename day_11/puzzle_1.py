from collections import Counter

with open("./day_11/real_data.txt") as reader:
    stones = [int(stone) for stone in reader.readline().strip().split()]

def blink(stone):
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        middle = len(str_stone) // 2
        new_stones.append(int(str_stone[:middle]))
        new_stones.append(int(str_stone[middle:]))
    else:
        new_stones.append(stone * 2024)
    return new_stones

stone_counts = Counter(stones)

for _ in range(25):
    new_stone_counts = Counter()
    for stone, count in stone_counts.items():
        new_stones = blink(stone)
        for new_stone in new_stones:
            new_stone_counts[new_stone] += count
    stone_counts = new_stone_counts

print(sum(stone_counts.values()))
