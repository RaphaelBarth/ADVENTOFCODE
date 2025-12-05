from timeit import default_timer as timer
import re
from aoc_utils.aoc import AoC

REGISTERS = {"A":None,"B":None,"C":None}
INSTRUCTION_POINTER = None

# define functions
def adv(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    REGISTERS["A"] = REGISTERS["A"]  >> combo_operand(operant)

def bxl(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    REGISTERS["B"] = REGISTERS["B"] ^ operant

def bst(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    REGISTERS["B"] = combo_operand(operant) % 8

def jnz(operant):
    global REGISTERS,INSTRUCTION_POINTER
    if REGISTERS["A"] == 0:
        INSTRUCTION_POINTER += 2
    else:
        INSTRUCTION_POINTER = operant

def bxc(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    REGISTERS["B"] = REGISTERS["B"] ^ REGISTERS["C"]

def out(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    return combo_operand(operant) % 8

def bdv(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    REGISTERS["B"] = REGISTERS["A"] >> combo_operand(operant)
    

def cdv(operant):
    global REGISTERS,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    REGISTERS["C"] = REGISTERS["A"] >> combo_operand(operant)


def combo_operand(operant):
    global REGISTERS
    match (operant):
            case 0,1,2,3:
                operant = operant
            case 4:
                operant = REGISTERS["A"]
            case 5:
                operant = REGISTERS["B"]
            case 6:
                operant = REGISTERS["C"]   
            case 7, _:
                raise Exception("unvalide combo operant")
    return operant



def start_program(program,register_A,register_B,register_C):
    global REGISTERS,INSTRUCTION_POINTER
    # initialize registers
    INSTRUCTION_POINTER = 0
    REGISTERS["A"] = register_A
    REGISTERS["B"] = register_B
    REGISTERS["C"] = register_C
    # run the program
    program = list(map(int,program.split(',')))
    return run_program(program=program)


# run programm
def run_program(program = ""):
    global INSTRUCTION_POINTER

    output_values = []
    while INSTRUCTION_POINTER < len(program):
        instruction,operant = program[INSTRUCTION_POINTER],program[INSTRUCTION_POINTER+1]
        #print(f"{instruction=}")
        match (instruction):
            case 0:
                adv(operant)
            case 1:
                bxl(operant)
            case 2:
                bst(operant)        
            case 3:
                jnz(operant)
            case 4:
                bxc(operant)                
            case 5:
                 output_values.append(out(operant))
            case 6:
                bdv(operant)
            case 7:
                cdv(operant)  

    return output_values


aoc = AoC(day=17, year=2024, use_example=False, use_example_nr=1)

register_a, register_b, register_c =tuple(map(int,re.findall(r"(\d+)\n",aoc.DATA)))
program = re.search(r"\d(,\d?)+",aoc.DATA).group()

timestamp = timer()
output = start_program(program,register_a,register_b,register_c)
output = ",".join(map(str,output))
#print(f"{output=} \n{REGISTERS=}") 
print(f"PART1: {output=} in {(timer())-timestamp}sec")

    
