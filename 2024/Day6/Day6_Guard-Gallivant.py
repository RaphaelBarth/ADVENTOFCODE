from enum import Enum, StrEnum
import re
from time import *
import numpy as np

temp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
DEBUG_PRINTING = False

class DIRECTION(StrEnum):
    UP='0'
    RIGHT='1'
    DOWN='2'
    LEFT='3'

    def new_direction(self) -> "DIRECTION":
        x = (int(self.value)+1)%4
        return DIRECTION(str(x))

def walk_field(field,limit = None):
    pos_y,pos_x = np.where(field=="^")
    direction = DIRECTION.UP

    limit_ctn =  -1 if not limit else limit
    while limit_ctn:
        limit_ctn = limit_ctn - 1  

        field[pos_y,pos_x] = 'x'
        match direction:
            case DIRECTION.UP:
                new_pos_y,new_pos_x = pos_y-1,pos_x
            case DIRECTION.DOWN:
                new_pos_y,new_pos_x = pos_y+1,pos_x
            case DIRECTION.LEFT:
                new_pos_y,new_pos_x = pos_y,pos_x-1
            case DIRECTION.RIGHT:
                new_pos_y,new_pos_x = pos_y,pos_x+1

        if new_pos_x == -1 or new_pos_y == -1 or new_pos_x  == field.shape[1] or new_pos_y == field.shape[0]:
            return field
    
        if field[new_pos_y,new_pos_x] == '#':
            if DEBUG_PRINTING:
                np.savetxt(fname="temp.txt",X=field,fmt="%s")
            direction = direction.new_direction()
        else:
            pos_x,pos_y = new_pos_x,new_pos_y
    # we reached the limit
    return None




with open("2024/Day6/Day6_data.txt") as file:
    data = file.read()
    field = np.array([list(line.strip()) for line in data.split('\n')])

    # part1
    resuld_field = walk_field(field.copy())
    print(np.count_nonzero(resuld_field == 'x'))

    # part2
    obstacles = 0
    guard_y,guard_x = np.where(field=="^")
    for iy, ix in np.ndindex(field.shape):
        if guard_x == ix and guard_y == iy:
            pass
        else:
            temp_field = field.copy()
            temp_field[iy,ix] = '#'
            obstacles += 1 if walk_field(temp_field,limit=10_000) is None else 0
            #print((iy, ix),obstacles)

    print(f"{obstacles=}")


