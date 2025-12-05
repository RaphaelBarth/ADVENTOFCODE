from timeit import default_timer as timer
from aoc_utils.aoc import AoC
import re
aoc = AoC(day=5, year=2025, use_example=False)



ingredient_ID_ranges = []
available_ingredient_IDs = []

for line in aoc.DATA.splitlines():
    if re.match(r"^\d+-\d+$", line.strip()):
        ingredient_ID_ranges.append(tuple(map(int,line.split('-'))))
    elif re.match(r"^\d+$", line.strip()):
        available_ingredient_IDs.append(int(line))
    else:
        pass

# start PART 1
timestamp1 = timer()

result = 0
for ingredient_ID in available_ingredient_IDs:
    for low,high in ingredient_ID_ranges:
        if low <= ingredient_ID <= high:
            result += 1
            break

print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")


# start PART 2
timestamp1 = timer()
ingredient_ID_ranges.sort()
ingredient_ID_ranges_merged = [ingredient_ID_ranges[0]]

for low, high in ingredient_ID_ranges[1:]:
    low_merged, high_merged = ingredient_ID_ranges_merged [-1]
    if low <= high_merged:
        ingredient_ID_ranges_merged [-1] = (low_merged,  max(high_merged, high))
    else:
        ingredient_ID_ranges_merged.append((low, high))

result = sum([high+1 - low for low, high in ingredient_ID_ranges_merged])

print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")
