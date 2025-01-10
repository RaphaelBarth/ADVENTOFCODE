import functools
from timeit import default_timer as timer
import re


example= """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

def check_design(design):
    if not len(design):
        return True
    for idx in reversed(range(len(design))):
        if design[idx:] in towel_patterns and check_design(design[:idx]):
            return True
    return False

@functools.cache
def count_design(design):
    if not len(design):
        return 1
    
    different_ways = 0
    for idx in reversed(range(len(design))):
        if design[idx:] in towel_patterns:
            different_ways+=count_design(design[:idx])
    return different_ways

with open("2024/Day19/data.txt") as file:
    data = file.read().splitlines()
    #data = example.splitlines()
    towel_patterns = data[0].split(', ')
    designs = data[2:]    

    ok = 0
    timestamp = timer()

    possible_designs = sum([check_design(design) for design in designs])
    print(f"PART1: {possible_designs=} in {(timer())-timestamp}sec")

    different_ways = sum([count_design(design) for design in designs])
    print(f"PART1: {different_ways=} in {(timer())-timestamp}sec")

            
            

    