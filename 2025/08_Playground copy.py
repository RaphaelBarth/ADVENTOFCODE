from functools import reduce
from timeit import default_timer as timer
from aoc_utils.aoc import AoC

aco = AoC(day=8, year=2025, use_example=True)
data = aco.DATA

junction_boxes = []
for data_line in data.split("\n"):
    x,y,z = map(int,data_line.split(","))
    junction_boxes.append((x,y,z))
#print(junction_boxes)


# calculate euclidean distance between two boxes
def calculate_distance(box1,box2):
    if box1 == box2:
        return float('inf')
    else:
        return ((box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2 )**0.5

# start PART 1
timestamp1 = timer()
#shortest_distance = {}
shortest_distance = []
for box in junction_boxes:
    nearest_box = min(junction_boxes, key=lambda b: calculate_distance(box,b))
    distance = calculate_distance(box,nearest_box)
    #shortest_distance[box] = nearest_box, distance
    shortest_distance.append((box,nearest_box,distance))

shortest_distance = sorted(shortest_distance, key=lambda x: x[2])

print(shortest_distance)
connections = 0
circuits = []
box_used_in_circuit = {}
for box,neighbor,_ in shortest_distance:
    # check if box is already in a circuit 
    if box in box_used_in_circuit and neighbor in box_used_in_circuit:
        continue
    if (circuit_id := box_used_in_circuit.get(box)) is not None:
        box_used_in_circuit[neighbor] = circuit_id
        circuits[circuit_id].add(neighbor)
    elif (circuit_id := box_used_in_circuit.get(neighbor)) is not None:
        box_used_in_circuit[box] = circuit_id
        circuits[circuit_id].add(box)
    else:
        circuit_id = len(circuits)
        circuits.append(set((box,neighbor)))
        box_used_in_circuit[box] = circuit_id
        box_used_in_circuit[neighbor] = circuit_id

    connections += 1
    if connections == 9:
        break

#print(box_used_in_circuit,sep="\n")
#print("------------------------")
#print(circuits)
result = reduce(lambda x, y: x * y, sorted(map(len, circuits))[-3:],1)   

print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")

