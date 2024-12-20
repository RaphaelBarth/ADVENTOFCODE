from collections import deque
from concurrent.futures import ThreadPoolExecutor
import functools
from threading import Thread
import numpy as np
from timeit import default_timer as timer


temp =  """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

def check_in_bounds(map,possition):
    max_y,max_x = map.shape
    cur_y,cur_x = possition
    if cur_y < 0 or cur_y >=max_y:
        return False
    if cur_x < 0 or cur_x >= max_x:
        return False
    return True


def find_connected_region(garden_map,fence_map,possition):
    if fence_map[possition] != -1:
        return
        
    garden_type = garden_map[possition]
    fence_map[possition] = 4

    for offset in [(0,1),(1,0),(0,-1),(-1,0)]:
        new_poss = tuple(np.add(possition,offset))
        if check_in_bounds(garden_map,new_poss) and garden_type == garden_map[new_poss]:
            fence_map[possition]-=1
            find_connected_region(garden_map,fence_map,new_poss)


def get_new_direction_offset(current = (-1,0)):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    temp = (directions.index(current)+1) % len(directions)
    return directions[temp]

def find_region_corners(garden_map,possition,start=None,previous_offset = (-1,0)):

    if possition == start:
        return 0
    
    if start is None:
        start = possition
        
    garden_type = garden_map[possition]
    corner = 0

    cur_direction=previous_offset
    new_poss = tuple(np.add(possition,cur_direction))
    if check_in_bounds(garden_map,new_poss) and garden_type == garden_map[new_poss]:
        pass
    else:
        while True:
            cur_direction = get_new_direction_offset(cur_direction)   
            new_poss = tuple(np.add(possition,cur_direction))
            if check_in_bounds(garden_map,new_poss) and garden_type == garden_map[new_poss]:
                break

    if cur_direction == previous_offset:
        corner += 0
    elif (0,0) in np.add(cur_direction,previous_offset):
        corner += 2
    else:
        corner += 1
    previous_offset = cur_direction
    corner += find_region_corners(garden_map,new_poss,start,previous_offset)
    return corner


with open("2024/Day12/data.txt") as file:
    data = file.read()
    data = temp

    timestamp = timer ()

    garden_map = np.array([list(line.strip()) for line in data.split('\n')],dtype=str)
    fence_map = np.full(garden_map.shape,dtype=int,fill_value=-1)

    total_costs_part1 = 0
    total_costs_part2 = 0
    previous_filled = 0
    previous_fences = 0
    while next_garden_list := list(zip(*np.where(fence_map == -1))):
        next_garden = next_garden_list[0]
        find_connected_region(garden_map,fence_map,next_garden)
        new_filled = np.count_nonzero(fence_map != -1) - previous_filled
        new_fences = np.sum(fence_map) + np.count_nonzero(fence_map == -1) - previous_fences
        total_costs_part1 += new_filled*new_fences
        previous_fences+=new_fences
        previous_filled+=new_filled

        sides = find_region_corners(garden_map,next_garden)
        total_costs_part1 += new_filled*sides


    print(f"PART1: {total_costs_part1=} in {(timer())-timestamp}sec")
    print(f"PART1: {total_costs_part2=} in {(timer())-timestamp}sec")

