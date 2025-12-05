from functools import reduce
import numpy as np
from timeit import default_timer as timer
from aoc_utils.aoc import AoC

aoc = AoC(day=9, year=2024, use_example=False)
FREE_SPACE = '.'
data = aoc.DATA

timestamp1 = timer()
data_blocks = []
data_block_id = 0
data_iter = iter([int(ele) for ele in data])

while (ele:=next(data_iter,None)) is not None:
    data_blocks.extend([data_block_id]*ele)
    data_block_id +=1
    if (ele := next(data_iter,None)) is None:
        continue
    data_blocks.extend([FREE_SPACE]*ele)


data_blocks = np.array(data_blocks)
while True:
    last_file_block = abs(np.argmax((data_blocks[::-1]) != FREE_SPACE) - (data_blocks.size-1))
    next_empty_block = np.argmax(data_blocks ==  FREE_SPACE)  
    if last_file_block > next_empty_block:
        data_blocks[next_empty_block] = data_blocks[last_file_block]
        data_blocks[last_file_block] = FREE_SPACE
    else:
        break

checksum = sum(int(ele)*idx for idx,ele in enumerate(data_blocks) if ele != FREE_SPACE)

print(f"PART1: {checksum=} in {(timestamp2:=timer())-timestamp1}sec")


# part 2
data_blocks = []
data_block_id = 0
data_iter = iter([int(ele) for ele in data])
while (ele:=next(data_iter,None)) is not None:
    data_blocks.append((data_block_id,ele))
    data_block_id +=1
    if (ele := next(data_iter,None)) is None:
        continue
    data_blocks.append((FREE_SPACE,ele))


for idx_rev in reversed(range(len(data_blocks))):
    ele_rev = data_blocks[idx_rev]
    if ele_rev[0] == '.':
        continue
    for idx_fwd in range(len(data_blocks[:idx_rev])):
        ele_fwd = data_blocks[idx_fwd]
        if ele_fwd[0] != '.':
            continue
        elif ele_fwd[1]<ele_rev[1]:
            continue
        else:
            data_blocks[idx_rev] = ('.',ele_rev[1])
            diff = ele_fwd[1] - ele_rev[1]
            data_blocks[idx_fwd] =  (ele_fwd[0],diff)
            data_blocks.insert(idx_fwd,ele_rev)
            break

temp = list(reduce(lambda x,y : x+[y[0]] *y[1],filter(lambda x: x[1] != 0,data_blocks),[]))
checksum = sum(int(ele)*idx for idx,ele in enumerate(temp) if ele != FREE_SPACE)

print(f"PART2: {checksum=} in {(timestamp1:=timer())-timestamp2}sec")

