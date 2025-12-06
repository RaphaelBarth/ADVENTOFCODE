example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

with open("./2025/day6.txt") as f:
    example = f.read()

numbers = []
for line in example.split("\n")[:-1]:
    x = line.split()
    numbers.append(list(map(int,x)))
opperators = [op for op in example.split("\n")[-1] if op != " "]
#print(numbers,opperators)


res = 0
for x in range(len(opperators)):
    temp = 0
    for number in numbers:
        if opperators[x] == "+":
            temp += number[x]
        elif opperators[x] == "*":
            temp = number[x] * (temp or 1)
        else:
            pass
    res+=temp
print(res)


numbers = []
for line in example.split("\n")[:-1]:
    x = [ele for ele in line]+[" "]
    numbers.append(x)

blub = []
bla = []
for x in range(len(numbers[0])):
    temp = ""
    for number in numbers:
        temp += number[x]
    if temp == len(numbers)*" ":
        blub.append(bla)
        bla = []
    else:
        bla.append(int(temp))


opperators = [op for op in example.split("\n")[-1] if op != " "]
#print(numbers,opperators)
res = 0
for x in range(len(opperators)):
    op,lis = opperators[x],blub[x]
    temp = 0
    for l in lis:
        if op == "+":
            temp += l
        elif op == "*":
            temp = l * (temp or 1)
        else:
            pass
    res+=temp

print(res)