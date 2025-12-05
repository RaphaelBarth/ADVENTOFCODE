import re
import numpy as np
from timeit import default_timer as timer
from aoc_utils.aoc import AoC


aoc = AoC(day=13, year=2024, use_example=False)
data = aoc.DATA

timestamp = timer()

claw_machines = []
data_iter = iter(data.strip().split('\n'))

#Part1
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
    
    B = np.array([c[0],c[1]],dtype=np.float64)

    C = np.linalg.solve(a=A,b=B)
    C1 = C[0]
    C2 = C[1]
    if C1 > 0 and C2 > 0 and np.round(C1,0) == np.round(C1,4) and np.round(C2,4) == np.round(C2,0):
        claw_machines.append((C1*3+C2))

tokens = sum(claw_machines)
print(f"PART1: {tokens=} in {(timer())-timestamp}sec")



#Part2
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

    B = np.array([c[0]+10000000000000,c[1]+10000000000000],dtype=np.float64)

    C = np.linalg.solve(a=A,b=B)
    C1 = C[0]
    C2 = C[1]
    if C1 > 0 and C2 > 0 and np.round(C1,0) == np.round(C1,4) and np.round(C2,4) == np.round(C2,0):
        claw_machines.append((C1*3+C2))

tokens = sum(claw_machines)
print(f"PART2: {tokens=} in {(timer())-timestamp}sec")

