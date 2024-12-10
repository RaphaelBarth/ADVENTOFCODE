import re
import math

with open("2024/Day3/data.txt") as file:
    data = file.read()
    mul_list = re.findall(r"mul\(\d+,\d+\)",data)
    print(sum([math.prod(list(map(int,re.findall(r"\d+",ele)))) for ele in mul_list]))


    #con_mul_list = re.findall("(do\(\)|don't\(\)).*?(mul\(\d+,\d+\))",data)
    #print(sum([math.prod(list(map(int,re.findall("\d+",ele)))) for con,ele in con_mul_list if con=="do()"]))

    enable = True
    con_mul_list = []
    for ele in re.findall(r"(do\(\)|don't\(\))|(mul\(\d+,\d+\))",data):
        ele = ele[0] or ele[1]
        if ele == "do()":
            enable = True
        elif ele == "don't()":
            enable = False
        elif enable:
            con_mul_list.append(ele)
        else:
            pass

    print(sum([math.prod(list(map(int,re.findall(r"\d+",ele)))) for ele in con_mul_list]))


