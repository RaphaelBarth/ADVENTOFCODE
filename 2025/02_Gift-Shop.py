from timeit import default_timer as timer
import re
from aoc_utils.aoc import AoC

aoc = AoC(day=2, year=2025, use_example=False)
data = aoc.DATA

timestamp1 = timer()

PATTERN_RANGE = r"[1-9]\d*-[1-9]\d*"
PATTERN_ID = r"^(\d+)\1$"

# Find all valid ranges in the data
valid_ranges = [x.split("-") for x in data.split(",") if re.match(PATTERN_RANGE, x)]
valid_ranges = [range(int(start), int(end)+1) for start, end in valid_ranges]

# Sum all valid IDs in the ranges
result = 0
for current_range in valid_ranges:    
    result+= sum([value for value in current_range if re.match(PATTERN_ID, str(value))])
    
print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")


timestamp1 = timer()
PATTERN_RANGE = r"[1-9]\d*-[1-9]\d*"
PATTERN_ID = r"^(\d+)\1+$"

# Find all valid ranges in the data
valid_ranges = [x.split("-") for x in data.split(",") if re.match(PATTERN_RANGE, x)]
valid_ranges = [range(int(start), int(end)+1) for start, end in valid_ranges]

# Calculate the sum of all valid IDs in the ranges
result = 0
for current_range in valid_ranges:    
    result+= sum([value for value in current_range if re.match(PATTERN_ID, str(value))])
    
print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")
