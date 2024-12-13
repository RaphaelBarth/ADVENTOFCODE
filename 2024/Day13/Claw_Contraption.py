import re
import numpy as np
from timeit import default_timer as timer


temp =  """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""




with open("2024/Day13/data.txt") as file:
    data = file.read()
    #data = temp

    timestamp = timer()

    claw_machines = []
    data_iter = iter(data.strip().split('\n'))
    while (line := next(data_iter,None)) is not None:
        if not line:
            continue
        
        a = tuple(int(match) for match in re.findall(r"\+(\d+)",line))
        line = next(data_iter)
        b = tuple(int(match) for match in re.findall(r"\+(\d+)",line))
        line = next(data_iter)
        c = tuple(int(match) for match in re.findall(r"=(\d+)",line))

        A = np.array([
            [a[0],b[0]],
            [a[1],b[1]]
            ],dtype=np.float64)
        
        #Part1
        B = np.array([c[0],c[1]],dtype=np.float64)
        #Part2
        B = np.array([c[0]+10000000000000,c[1]+10000000000000],dtype=np.float64)

        C = np.linalg.solve(a=A,b=B)
        C1 = C[0]
        C2 = C[1]
        print(C1,C2)
        if C1 > 0 and C2 > 0 and np.round(C1,0) == np.round(C1,4) and np.round(C2,4) == np.round(C2,0):
            claw_machines.append((C1*3+C2))

    tokens = sum(claw_machines)
    print(f"PART*: {tokens=} in {(timer())-timestamp}sec")

