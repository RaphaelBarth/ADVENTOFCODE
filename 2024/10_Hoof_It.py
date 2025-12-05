import numpy as np
from timeit import default_timer as timer


temp =  """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def check_in_map(topographic_map,possition):
    y_map,x_map = topographic_map.shape
    y_pos,x_pos = possition
    if y_pos < 0 or y_pos >= y_map:
        return False
    if x_pos < 0 or x_pos >= x_map:
        return False
    return True

def hiking(topographic_map,possition ):
    if topographic_map[possition] == 9:
        return 1
    
    trailheads  = 0
    current_hight = topographic_map[possition]
    for direction in [(0,1),(1,0),(-1,0),(0,-1)]:
        new_possition = tuple(np.add(possition,direction))
        if check_in_map(topographic_map,new_possition) and (topographic_map[new_possition]) == (current_hight+1):
            trailheads += hiking(topographic_map,new_possition)

    return trailheads

def hiking_scores(topographic_map,possition):
    if topographic_map[possition] == 9:
        return possition
    
    trailheads  = []
    current_hight = topographic_map[possition]
    for direction in [(0,1),(1,0),(-1,0),(0,-1)]:
        new_possition = tuple(np.add(possition,direction))
        if check_in_map(topographic_map,new_possition) and (topographic_map[new_possition]) == (current_hight+1):
            trailheads += hiking_scores(topographic_map,new_possition)

    return trailheads


with open("2024/Day10/data.txt") as file:
    data = file.read()
    #data = temp

    timestamp1 = timer()
    topographic_map = np.array([list(line.strip()) for line in data.split('\n')],dtype=int)
    starting_points = list(zip(*np.where(topographic_map == 0)))
    target_points = list(zip(*np.where(topographic_map == 9)))


    trailheads_score = [hiking_scores(topographic_map,starting_point) for starting_point in starting_points]
    trailheads_score = sum([len(set(zip(trail[::2], trail[1::2]))) for trail in trailheads_score])
    print(f"PART1: {trailheads_score=} in {(timestamp2:=timer())-timestamp1}sec")
        

 
    

    trailheads_score = sum([hiking(topographic_map,starting_point) for starting_point in starting_points])
    print(f"PART1: {trailheads_score=} in {(timestamp2:=timer())-timestamp1}sec")

