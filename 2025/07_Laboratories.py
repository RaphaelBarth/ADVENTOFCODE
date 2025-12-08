from timeit import default_timer as timer
from functools import cache
from aoc_utils.aoc import AoC

aco = AoC(day=7, year=2025, use_example=False)
data = aco.get_stream()

# Read the initial beam positions and splitter positions
beams_per_line = [i for i, x in enumerate(data.readline()) if x == "S"]
splitters_per_line = []
for line in data.readlines():
    splitters_per_line.append([i for i, x in enumerate(line) if x == "^"])
#print(beams_per_line,splitters_per_line)

# start PART 1
timestamp1 = timer()

splitted = 0
new_beams_per_line=set()
current_beams_per_line= set(beams_per_line)
for splitters in splitters_per_line:
    for beam in current_beams_per_line:
        if beam in splitters:
            new_beams_per_line.add(beam-1)
            new_beams_per_line.add(beam+1)
            splitted+=1
        else:
            new_beams_per_line.add(beam)

    current_beams_per_line = new_beams_per_line
    new_beams_per_line = set()

print(f"PART1: {splitted=} in {(timestamp2:=timer())-timestamp1}sec")

# start PART 2
timestamp1 = timer()
depth = len(splitters_per_line)

@cache
def calculate_beam_paths(current_depth:int,beam:int):
    paths = 0
    if (depth) == current_depth:
        return 1
    if (beam in splitters_per_line[current_depth]):
        paths += calculate_beam_paths(current_depth+1,beam+1)
        paths += calculate_beam_paths(current_depth+1,beam-1)
    else:
        paths += calculate_beam_paths(current_depth+1,beam)
    return paths
    

beam = beams_per_line[0]   
print(f"PART2: {calculate_beam_paths(0,beam)=} in {(timestamp2:=timer())-timestamp1}sec")