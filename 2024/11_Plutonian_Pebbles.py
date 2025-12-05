from collections import deque
import functools
import numpy as np
from timeit import default_timer as timer
from aoc_utils.aoc import AoC


aoc = AoC(day=11, year=2024, use_example=True)
data = aoc.DATA


@functools.cache
def apply_rules(input) ->  list:
    if input == 0:
        return [1]
    elif len(input_str := str(input)) % 2 == 0:
        middle = len(input_str)//2
        return [int(input_str[:middle]),int(input_str[middle:])]
    else:
        return [input*2024]

def apply_rules_deque(input:deque) -> deque: 
    output = deque()
    for ele in input:
        output.extend(apply_rules(ele))
    return output


initial_arrangement = np.array(data.split(),dtype=int)

timestamp = timer ()
arrangement = deque(iterable=initial_arrangement)
for i in range(25):
    arrangement = apply_rules_deque(arrangement)
    #print(arrangement)

stones = len(arrangement)
print(f"PART1: {stones=} in {(timer())-timestamp}sec")

timestamp = timer ()
arrangement = deque(iterable=initial_arrangement)
for iteration in range(75):
    timestamp1 = timer()
    arrangement = apply_rules_deque(arrangement)
    print(f"{iteration=} in {timer()-timestamp1}")

stones = len(arrangement)
print(f"PART2: {stones=} in {(timer())-timestamp}sec")

