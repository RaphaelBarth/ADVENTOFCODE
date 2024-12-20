import re
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from timeit import default_timer as timer


temp =  """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

SHAPE_X = 101
SHAPE_Y = 103

SECONDS = 100

def do_step(possition,velocity):
    new_x = (possition[0] + velocity[0]) % SHAPE_X
    new_y = (possition[1] + velocity[1]) % SHAPE_Y
    return new_x,new_y


with open("2024/Day14/data.txt") as file:
    data = file.read()
    #data = temp

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
        fig.savefig(f"2024/Day14/temp/{second}.txt")

        if second == SECONDS:
            quad_y = SHAPE_Y // 2
            quad_x = SHAPE_X // 2
            safety_factor = np.sum(grid[:quad_y,:quad_x]) * np.sum(grid[-quad_y:,:quad_x]) * np.sum(grid[:quad_y,-quad_x:]) * np.sum(grid[-quad_y:,-quad_x:])
            print(f"PART2: {safety_factor=}")



    anim = FuncAnimation(fig,update,interval=1)
    plt.show()

