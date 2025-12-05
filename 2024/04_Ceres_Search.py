import numpy as np
import re
from aoc_utils.aoc import AoC

aoc = AoC(day=4, year=2024, use_example=False)


data = aoc.DATA
matrix = np.array([list(line) for line in data.strip().split('\n')])

horizontal = [str().join(line) for line in matrix]
vertical = [str().join(line) for line in matrix.transpose()]
diagonal1 = [str().join(matrix.diagonal(offset=idx)) for idx in range(-(matrix.shape[0]-1),(matrix.shape[1]-1))]
diagonal2 = [str().join(np.rot90(matrix).diagonal(offset=idx)) for idx in range(-(matrix.shape[0]-1),(matrix.shape[1]-1))]

count = sum([(lis.count("XMAS") + lis.count("SAMX")) for lis in (horizontal+vertical+diagonal1+diagonal2)])
print(count)


data = data.split()
x,y = len((tmp := data)[0]), len(tmp)
count = 0
for idx_y in range(y-2):
    for idx_x in range(x-2):
        
        sub_string = str(data[idx_y+0][idx_x:idx_x+3]+data[idx_y+1][idx_x:idx_x+3]+data[idx_y+2][idx_x:idx_x+3])
        count += 1 if re.findall("M.S.A.M.S",sub_string) else 0
        count += 1 if re.findall("S.M.A.S.M",sub_string) else 0
        count += 1 if re.findall("M.M.A.S.S",sub_string) else 0
        count += 1 if re.findall("S.S.A.M.M",sub_string) else 0
        
print(count)

