from timeit import default_timer as timer
import numpy as np
from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aoc = AoC(day=4, year=2025, use_example=False)
data = aoc.DATA

# start PART 1
timestamp1 = timer()

# Create grid
grid = np.matrix(list(map(list, data.split())) )

result = 0
# Iterate through each position in the grid
for x in range(0,(x_max:=grid.shape[0])):
    for y in range(0,(y_max:=grid.shape[1])):
        x_left = max(0,x-1)
        x_right = min(x_max,x+2)
        y_down = max(0,y-1)
        y_up = min(y_max,y+2)

        # create block around current position
        grid_block = grid[x_left:x_right,y_down:y_up]
        # check if current position is '@' and count of '@' in block is less than or equal to 4
        if grid[x,y] == '@' and np.count_nonzero(grid_block == '@') <= 4:   
            result+= 1

print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")

# start PART 2
timestamp1 = timer()
# Create grid
grid = np.matrix(list(map(list, data.split())) )

result = 0
# Repeat until no more positions can be removed
done_flag = False 
while not done_flag:
    remove = list()
    # Iterate through each position in the grid
    for x in range(0,(x_max:=grid.shape[0])):
        for y in range(0,(y_max:=grid.shape[1])):
            x_left = max(0,x-1)
            x_right = min(x_max,x+2)
            y_down = max(0,y-1)
            y_up = min(y_max,y+2)

            grid_block = grid[x_left:x_right,y_down:y_up]
            if grid[x,y] == '@' and np.count_nonzero(grid_block == '@') <= 4:   
                remove.append((x,y))

    # Remove positions marked for removal
    for x,y in remove:
        grid[x,y] = 'x'

    # If no positions were removed, we are done   
    done_flag = True if not remove else False
    # Count removed '@' symbols
    result += len(remove)

print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")


