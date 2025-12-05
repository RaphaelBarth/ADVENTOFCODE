from itertools import combinations
import numpy as np
from aoc_utils.aoc import AoC

def is_out_of_bound(index,grid):
    y,x = grid.shape
    if index[0] >= y or index[0] < 0:
        return True
    if index[1] >= x or index[1] < 0:
        return True
    return False

aoc = AoC(day=8, year=2024, use_example=False)
data = aoc.DATA
# get the frequencies
frequencies  = set(data.replace(".","").replace("\n",""))
print(f"{frequencies=}")
# convert the input to np array
antenna_grid = np.array([list(line.strip()) for line in data.split('\n')])

# extract some caluculation data
antennas =  {frequency:np.transpose((antenna_grid == frequency).nonzero()) for frequency in frequencies}
for frequencie,antenna in antennas.items():
        antennas[frequencie] = list(combinations(antenna,2))

# part 1
antinode_grid = np.zeros(antenna_grid.shape,dtype=int)
for frequencie,antenna_combinations in antennas.items():
    for antenna_combination in antenna_combinations:
        offset = np.subtract(antenna_combination[0], antenna_combination[1])
        antinode1 = np.subtract(antenna_combination[1],offset)
        antinode2 = np.add(antenna_combination[0],offset)
        if not is_out_of_bound(antinode1,antenna_grid):
            antinode_grid[tuple(antinode1)] = 1
        if not is_out_of_bound(antinode2,antenna_grid):
            antinode_grid[tuple(antinode2)] = 1
# print the result 
print(np.sum(antinode_grid,where=[1]))


# part 2
antinode_grid = np.zeros(antenna_grid.shape,dtype=int)
for frequencie,antenna_combinations in antennas.items():
    for antenna_combination in antenna_combinations:
        offset = np.subtract(antenna_combination[0], antenna_combination[1])
        for step in range(antinode_grid.shape[0]):
                new_offset = offset*step
                antinode1 = np.subtract(antenna_combination[1],new_offset)
                antinode2 = np.add(antenna_combination[0],new_offset)
                if not is_out_of_bound(antinode1,antenna_grid):
                    antinode_grid[tuple(antinode1)] = 1
                if not is_out_of_bound(antinode2,antenna_grid):
                    antinode_grid[tuple(antinode2)] = 1
print(np.sum(antinode_grid,where=[1]))




