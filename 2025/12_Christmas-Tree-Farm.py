import re
from timeit import default_timer as timer

import numpy as np
from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aoc = AoC(day=12, year=2025, use_example=False)
data_stream = aoc.get_stream()

presents_shape = []
presents_regions = []
while (line:= data_stream.readline()):
    # if line matches shape pattern (e.g., "1:", "2::"), read the next 3 lines as shape
    if re.match(r"^\d:*$", line):
        rows = [next(data_stream).strip() for _ in range(3)]
        # convert rows to boolean matrix and store
        matrix = np.matrix([[True if char == '#' else False for char in row] for row in rows])
        presents_shape.append(matrix)
    # if the line is empty, skip
    elif line.strip() == "":
        pass
    # else if line is region
    else:
        # pattern (e.g., "5x4: 1 2 3"), extract dimensions and shapes
        PATTERN = r"(\d+)x(\d+): (.*)"
        matches = re.match(PATTERN, line).groups()
        width, height, shapes = (matches)
        region = (int(width), int(height)),list(map(int, shapes.split()))
        presents_regions.append(region)

#print(presents_regions, sep="\n")
#print(presents_shape, sep="\n")

        
timestamp1 = timer()
result = 0
# for each region, check if the total worst-case area of shapes fits in the region
for (width , height) , shapes in presents_regions:
    result += 1 if sum(shapes)*9 <= width * height else 0

print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")