from itertools import combinations
from timeit import default_timer as timer
from shapely import Polygon
from matplotlib import pyplot as plt
from aoc_utils.aoc import AoC


aco = AoC(day=9, year=2025, use_example=False)
data = aco.DATA

# parse input data to list of tuples
tiles = []
tiles = [tuple(map(int, line.split(","))) for line in data.split("\n")]
#print(tiles)

# start PART 1
timestamp1 = timer()

# function to calculate rectangle area between two tiles
def compute_rectangle_area(tile1, tile2) -> int:
    if tile1 == tile2:
        return 0
    else:
        return int((abs(tile1[0]-tile2[0])+1) * (abs(tile1[1]-tile2[1])+1))

largest_rectangles = []
for tile in tiles:
    rectangle = max(tiles, key=lambda b: compute_rectangle_area(tile,b))
    #print(f"{tile=} {rectangle=} {calculate_rectangle(tile,rectangle)=}")
    largest_rectangles.append(compute_rectangle_area(tile,rectangle))

largest_rectangle = max(largest_rectangles)
print(f"PART1: {largest_rectangle=} in {(timestamp2:=timer())-timestamp1}sec")

# start PART 2
timestamp1 = timer()

# create polygon from tiles
polygon = Polygon(tiles)

largest_rectangles = []
# get all combinations of two tiles to form rectangles
for combined_tiles in list(combinations(tiles, 2)):
    # form rectangle from two tiles
    rectangle = [combined_tiles[0],(combined_tiles[0][0],combined_tiles[1][1]),combined_tiles[1],(combined_tiles[1][0],combined_tiles[0][1])]
    # check if rectangle is fully inside polygon
    if polygon.contains(Polygon(rectangle)):
        largest_rectangles.append((compute_rectangle_area(rectangle[0],rectangle[2]),rectangle))

# find the rectangle with the largest area
largest_rectangle = max(largest_rectangles, key=lambda x: x[0])
print(f"PART2: {largest_rectangle[0]=} in {(timestamp2:=timer())-timestamp1}sec")

# plotting for visualization
plt.plot(*polygon.exterior.xy)
print(largest_rectangle[1])
plt.plot(*zip(*largest_rectangle[1], largest_rectangle[1][0]), color='red')
plt.show()
