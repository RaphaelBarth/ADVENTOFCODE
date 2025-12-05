from aoc_utils.aoc import AoC

def differ(lis):
    for idx in range(1,len(lis)):
        diff = abs(lis[idx-1] -lis[idx])
        if diff < 1 or diff > 3:
            return False
    return True 

def ordered(ele):
    return (ele == sorted(ele)) or (ele == sorted(ele,reverse=True))


aoc = AoC(day=2, year=2024, use_example=False) 
data = [list(map(int, line.split())) for line in aoc.DATA.splitlines()]


safe_reports = new_save_reports= 0
for ele in data:
    if ordered(ele) and differ(ele):
        safe_reports += 1
    else: # this is part 2
        for idx in range(len(ele)):
            tmp = ele[::]
            del tmp[idx] 
            if ordered(tmp) and differ(tmp):
                new_save_reports+=1
                break

new_save_reports +=safe_reports      
print(f"{safe_reports=}")
print(f"{new_save_reports=}")
