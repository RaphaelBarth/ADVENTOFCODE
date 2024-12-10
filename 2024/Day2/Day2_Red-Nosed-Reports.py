
def differ(lis):
    for idx in range(1,len(lis)):
        diff = abs(lis[idx-1] -lis[idx])
        if diff < 1 or diff > 3:
            return False
    return True 

def ordered(ele):
    return (ele == sorted(ele)) or (ele == sorted(ele,reverse=True))

with open("Day2_data.txt") as data:
    data = [list(map(int, line.strip().split())) for line in data]
    
    reports= 0
    for ele in data:
        if ordered(ele) and differ(ele):
            reports += 1
        else:
            for idx in range(len(ele)):
                tmp = ele[::]
                del tmp[idx] 
                if ordered(tmp) and differ(tmp):
                    reports+=1
                    break
                
    print(reports)
