from timeit import default_timer as timer
from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aoc = AoC(day=6, year=2025, use_example=False)
data = aoc.DATA

# start PART 1
timestamp1 = timer()

# parse input for part1 to list of numbers and operators
numbers = []
for line in data.split("\n")[:-1]:
    x = line.split()
    numbers.append(list(map(int,x)))
operators = [op for op in data.split("\n")[-1] if op != " "]

# compute result for part 1 for each column of numbers with corresponding operator
result = 0
for x in range(len(operators)):
    temp = 0
    for number in numbers:
        if operators[x] == "+":
            temp += number[x]
        elif operators[x] == "*":
            temp = number[x] * (temp or 1)
        else:
            pass
    # sum up all column results
    result+=temp

print(f"PART1: {result=} in {(timestamp2:=timer())-timestamp1}sec")


# start PART 2
timestamp1 = timer()

# parse input for part2 to list of numbers and opperators
operators = [op for op in data.split("\n")[-1] if op != " "]

# create a 2D list (row x column) of string numbers where each column separated by " " belongs to an operator 
numbers_array = []
for line in data.split("\n")[:-1]:
    x = [ele for ele in line]+[" "]
    numbers_array.append(x)

#get the the numbers for each operator column
numbers_per_operator = []
int_numbers = []
for column in range(len(numbers_array[0])):
    str_number = ""
    # build the string number for this operator column
    for number in numbers_array:
        str_number += number[column]
    # if the string number is only spaces, we finished one operator column so save the current list of integer numbers and reset for next operator column
    if str_number == len(numbers_array)*" ":
        numbers_per_operator.append(int_numbers)
        int_numbers = []
    else:
        # convert the string number to integer and add to current operator column list
        int_numbers.append(int(str_number))


result = 0
# compute result for part 2 for each column of numbers with corresponding operator
for x in range(len(operators)):
    # get the operator and the list of numbers for this column
    op,numbers = operators[x],numbers_per_operator[x]
    temp = 0
    # for each number in this column, apply the operator
    for number in numbers:
        if op == "+":
            temp += number
        elif op == "*":
            temp = number * (temp or 1)
        else:
            pass
    # sum up all column results
    result+=temp

print(f"PART2: {result=} in {(timestamp2:=timer())-timestamp1}sec")