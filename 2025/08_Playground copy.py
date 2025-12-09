from functools import reduce
from timeit import default_timer as timer
from itertools import combinations
from aoc_utils.aoc import AoC

aco = AoC(day=8, year=2025, use_example=False)
data = aco.DATA

junction_boxes = []
for data_line in data.split("\n"):
    junction_boxes.append(tuple(map(int,data_line.split(","))))
#print(junction_boxes)

# calculate euclidean distance between two boxes
def calculate_distance(box1,box2):
    if box1 == box2:
        return float('inf')
    else:
        return ((box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2 )**0.5

# start PART 1
timestamp1 = timer()
distance_map = {}
# calculate distance map between all junction boxes
for combination in combinations(junction_boxes, 2):
    distance = calculate_distance(combination[0],combination[1])
    distance_map.update({distance: combination})

timestamp2 = None
circuit_sizes = None
final_connection = None

# function to add boxes to circuits
def add_box_to_circuit(box1, box2,circuits_map):
    # merge circuits if both boxes are already in circuits
    if box1 in circuits_map and box2 in circuits_map:
        circuit1 = circuits_map[box1]
        circuit2 = circuits_map[box2]
        circuit1.update(circuit2)
        for box in circuit2:
            circuits_map[box] = circuit1        
    # add box2 to existing circuit of box1
    elif box1 in circuits_map:
        circuit = circuits_map[box1]
        circuits_map[box2] = circuit
        circuit.update([box2])
    # add box1 to existing circuit of box2
    elif box2 in circuits_map:
        circuit = circuits_map[box2]
        circuits_map[box1] = circuit
        circuit.update([box1])
    # create new circuit with both boxes
    else:
        circuit = set([box1, box2])
        circuits_map[box1] = circuit
        circuits_map[box2] = circuit
    return circuits_map

result = None
connections = 0
circuits_map = {}
# process connections to form circuits
for distance in sorted(distance_map.keys()):
    box1, box2 = distance_map[distance]
    circuits_map = add_box_to_circuit(box1, box2, circuits_map)
    
    # PART 1 limit to first n-connections 
    connections += 1
    if connections == 10_000:
        circuits_unique = set(map(frozenset, circuits_map.values()))
        circuit_sizes = sorted(map(len, circuits_unique), reverse=True)
        result = reduce(lambda a,b: a*b, circuit_sizes[:3], 1)
        break        

# print circuit sizes result for PART 1
print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")


# start PART 2
timestamp1 = timer()

circuits_map = {}
for distance in sorted(distance_map.keys()):
    box1, box2 = distance_map[distance]
    circuits_map = add_box_to_circuit(box1, box2, circuits_map)

    # PART 2 process all connections
    if len(junction_boxes) == len(circuits_map[box1]): 
        final_connection = (box1, box2)
        break

# print final connections result for PART 2
result = final_connection[0][0] * final_connection[1][0]
print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")

