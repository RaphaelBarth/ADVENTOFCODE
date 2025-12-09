from timeit import default_timer as timer
from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aoc = AoC(day=3, year=2025, use_example=False)
data = aoc.DATA


timestamp1 = timer()
result = 0
# process each line to find the two largest joltage ratings
for line in data.split():
    line = list(map(int, line))
    idx = line.index((val1:=max(line[:-1])))
    line[idx+1:].index((val2:=max(line[idx+1:])))
    
    result+= int(val1)*10+int(val2)
    
print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")


timestamp1 = timer()

result = 0
# process each line to find the twelve largest joltage ratings 
for line in data.split():
    line = list(map(int, line))
    idx = 0
    idx += line[idx:].index((val1:=max(line[idx:-11]))) +1
    idx += line[idx:].index((val2:=max(line[idx:-10]))) +1
    idx += line[idx:].index((val3:=max(line[idx:-9]))) +1
    idx += line[idx:].index((val4:=max(line[idx:-8]))) +1 
    idx += line[idx:].index((val5:=max(line[idx:-7]))) +1
    idx += line[idx:].index((val6:=max(line[idx:-6]))) +1
    idx += line[idx:].index((val7:=max(line[idx:-5]))) +1
    idx += line[idx:].index((val8:=max(line[idx:-4]))) +1
    idx += line[idx:].index((val9:=max(line[idx:-3]))) +1
    idx += line[idx:].index((val10:=max(line[idx:-2]))) +1
    idx += line[idx:].index((val11:=max(line[idx:-1]))) +1
    idx += line[idx:].index((val12:=max(line[idx:]))) +1

    #print(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12)
    result+= (val1*10**11)+(val2*10**10)+(val3*10**9)+(val4*10**8)+(val5*10**7)+(val6*10**6)+(val7*10**5)+(val8*10**4)+(val9*10**3)+(val10*10**2)+(val11*10**1)+val12

print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")



#def find_largest_joltage(data,digits) -> int:
#    result = 0
#    for line in data.split():
#        line,index = list(map(int, line)),0
#        for digit in range(-(digits-1),1):
#            index += line[index:].index((val:=max(line[index:(digit if digit!= 0 else None)])))+1
#            result+= val * (10**(digits+digit-1))
#        print(result)
#    return result
#print(find_largest_joltage(data,12))



    
