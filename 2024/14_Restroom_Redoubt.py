import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from timeit import default_timer as timer
from aoc_utils.aoc import AoC

SHAPE_X = 101
SHAPE_Y = 103

SECONDS = 100

def do_step(possition,velocity):
    new_x = (possition[0] + velocity[0]) % SHAPE_X
    new_y = (possition[1] + velocity[1]) % SHAPE_Y
    return new_x,new_y


aoc = AoC(day=14, year=2024, use_example=False)
data = aoc.DATA

timestamp = timer()

parse_input = [list(map(int,entry)) for entry in re.findall(r"p=(-?\d+),(-?\d+).*v=(-?\d+),(-?\d+)\n?",data)]
parse_input = list(map(lambda entry: list(zip(entry[::2],entry[1::2])),parse_input))



grid = np.zeros((SHAPE_Y,SHAPE_X),dtype=int)
for robot in parse_input:
    possition,velocity = robot
    for second in range(SECONDS):
        possition = do_step(possition,velocity)
    grid[possition[1],possition[0]] +=1

quad_y = SHAPE_Y // 2
quad_x = SHAPE_X // 2

safety_factor = np.sum(grid[:quad_y,:quad_x]) * np.sum(grid[-quad_y:,:quad_x]) * np.sum(grid[:quad_y,-quad_x:]) * np.sum(grid[-quad_y:,-quad_x:])
print(f"PART1: {safety_factor=} in {(timer())-timestamp}sec")

second = 0
fig, ax = plt.subplots()
ax.set_ylim(SHAPE_Y)
ax.set_xlim(SHAPE_X)
grid = np.zeros((SHAPE_Y,SHAPE_X),dtype=int)
def update(frame):
    global second, highest
    second += 1

    robot_possition = []
    for robot in parse_input:
        robot[0] = (possition:= do_step(robot[0],robot[1]))
        robot_possition.append(possition)

        if second == SECONDS:
            grid[possition[1],possition[0]] +=1


    x,y = zip(*robot_possition)
    ax.clear()
    ax.scatter(x,y)
    fig.canvas.draw()
    fig.savefig(f"2024/temp/14_Restroom_Redoubt_{second}.txt")

    if second == SECONDS:
        quad_y = SHAPE_Y // 2
        quad_x = SHAPE_X // 2
        safety_factor = np.sum(grid[:quad_y,:quad_x]) * np.sum(grid[-quad_y:,:quad_x]) * np.sum(grid[:quad_y,-quad_x:]) * np.sum(grid[-quad_y:,-quad_x:])
        print(f"PART2: {safety_factor=}")



anim = FuncAnimation(fig,update,interval=1)
plt.show()

