from enum import Enum, StrEnum
from functools import reduce
import numpy as np
from time import *
import numpy as np

temp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def is_calculable_2(equation):
    expected_result,operands = equation[0],equation[1]
    operantors_n = len(operands)-1

    combinations = list(map(lambda x : list(np.base_repr(x,base=3).zfill(operantors_n)),  range(3**operantors_n)))
    for combination in combinations:

        result = operands[0]   
        for operand in operands[1::]:
            match combination.pop():
                case '0':
                    result = result + operand
                case '1':
                    result = result * operand
                case '2':
                    result = int(str(result)+str(operand))

        if result == expected_result:
            return True
        
    return False

def is_calculable_1(equation):
    expected_result,operands = equation[0],equation[1]
    operantors_n = len(operands)-1

    combinations = list(map(lambda x : list(format(x,f'0{operantors_n}b')),  range(2**operantors_n)))
    for combination in combinations:
        result = reduce(lambda x,y: x+y if combination.pop() == '0' else x*y ,operands)

        if result == expected_result:
            return True
        
    return False


with open("2024/Day7/data.txt") as file:
    data = file.read()
    equations = []
    for line in data.splitlines():
        left, right = line.split(':')
        right = list(map(int,right.split()))
        left = int(left)
        equations.append((left,right))

    valide_calibration_results = [equation[0] for equation in equations if is_calculable_1(equation)]
    print (sum(valide_calibration_results))

    valide_calibration_results = [equation[0] for equation in equations if is_calculable_2(equation)]
    print (sum(valide_calibration_results))



