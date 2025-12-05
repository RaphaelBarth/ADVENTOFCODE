from timeit import default_timer as timer
import re
EXAMPLE = False
if EXAMPLE: 
    data ="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
else:
    with open("2025/Day2/data.txt") as f:
        data = f.read().strip()


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
