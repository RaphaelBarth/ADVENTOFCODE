from enum import Enum, StrEnum
import re
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

class DIRECTION(StrEnum):
    UP='0'
    RIGHT='1'
    DOWN='2'
    LEFT='3'

    def new_direction(self) -> "DIRECTION":
        x = (int(self.value)+1)%4
        return DIRECTION(str(x))

with open("2024/Day6/Day6_data.txt") as file:
    data = file.read()
    field = np.array([list(line.strip()) for line in data.split('\n')])

    pos_y,pos_x = np.where(field=="^")
    direction = DIRECTION.UP

    while True:
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
            break
    
        if field[new_pos_y,new_pos_x] != '#':
            pos_x,pos_y = new_pos_x,new_pos_y
        else:
            direction = direction.new_direction()

    print(np.count_nonzero(field == 'x'))


with open("2024/Day6/Day6_data.txt") as file:
    data = temp#file.read()
    field = np.array([list(line.strip()) for line in data.split('\n')])

    pos_y,pos_x = np.where(field=="^")
    pos_y,pos_x = pos_y[0] ,pos_x[0]
    direction = DIRECTION.UP
    positions =0
    
    while True:
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
            break
        
        #np.savetxt(fname="temp.txt",X=field,fmt="%s")
        match direction:
            case DIRECTION.UP:
                lis = [ele for ele in field[pos_y,pos_x+1:]]
            case DIRECTION.DOWN:
                lis = [ele for ele in field[pos_y,pos_x-1::-1]]
            case DIRECTION.LEFT:
                lis = [ele for ele in field[pos_y-1::-1,pos_x] ]
            case DIRECTION.RIGHT:
                lis = [ele for ele in field[pos_y+1::,pos_x]]

        x = str.join("",lis)
        if lis and re.findall(".*x#",x):
            positions+=1
        

        if field[new_pos_y,new_pos_x] != '#':
            pos_x,pos_y = new_pos_x,new_pos_y
        else:
            direction = direction.new_direction()
            #field[field==direction]='.'


    print(positions)


