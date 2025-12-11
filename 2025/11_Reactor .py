import functools

from timeit import default_timer as timer
from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aoc = AoC(day=11, year=2025, use_example=False, use_example_nr=2)

# read device connections from input
connections = {}
for line in aoc.get_stream().readlines():
    device,outputs = line.split(":")
    connections[device.strip()] = [out.strip() for out in outputs.split()]
#print(f"{connections=}")

# function to find all paths from current to end using DFS
@functools.cache
def find_path(current, end, required_visits = ()) -> int:
    # if current is in visit list, remove it
    if current in required_visits:
        idx = required_visits.index(current)
        required_visits = required_visits[:idx] + required_visits[idx+1:]

    # if current is the end node, found a path
    if current == end:
        return 1 if not required_visits else 0
    
    # recursively explore all connected nodes
    found_paths = 0
    for node in connections[current]:
        found_paths += find_path(node, end,required_visits)  
    return found_paths


# start PART 1
timestamp1 = timer()
result = find_path("you", "out")
print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")

# start PART 2
timestamp1 = timer()


result = find_path("svr", 'out', required_visits=("fft","dac"))
print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")