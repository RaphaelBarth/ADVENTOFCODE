
example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""



import io
data = io.StringIO(example)

data = open("./2025/day6.txt") 

beams_per_line = [i for i, x in enumerate(data.readline()) if x == "S"]

splitters_per_line = []
for line in data.readlines():
    splitters_per_line.append([i for i, x in enumerate(line) if x == "^"])

#print(beams_per_line,splitters_per_line)

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

print(splitted)

depth = len(splitters_per_line)

from functools import cache
@cache
def xyz(current_depth:int,beam:int):
    paths = 0
    if (depth) == current_depth:
        return 1
    if (beam in splitters_per_line[current_depth]):
        paths += xyz(current_depth+1,beam+1)
        paths += xyz(current_depth+1,beam-1)
    else:
        paths += xyz(current_depth+1,beam)
    return paths
    

beam = beams_per_line[0]   
print(xyz(0,beam))