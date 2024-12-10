
def differ(lis):
    for idx in range(1,len(lis)):
        diff = abs(lis[idx-1] -lis[idx])
        if diff < 1 or diff > 3:
            return False
    return True 

def ordered(ele):
    return (ele == sorted(ele)) or (ele == sorted(ele,reverse=True))

with open("2024/Day2/data.txt") as file:
    data = file
    data = [list(map(int, line.strip().split())) for line in data]
    
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
