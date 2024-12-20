

# Create registers
A = None
B = None
C = None
INSTRUCTION_POINTER = None


# define functions
def adv(combo_operand=0,literal_operand = 0):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    A = A // (combo_operand**2)

def bxl(combo_operand=1,literal_operand = 1):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    B = B ^ literal_operand

def bst(combo_operand=2,literal_operand = 2):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    B = combo_operand % 8

def jnz(combo_operand=3,literal_operand = 3):
    global A,B,C,INSTRUCTION_POINTER
    if A == 0:
        INSTRUCTION_POINTER += 2
    else:
        INSTRUCTION_POINTER = combo_operand

def bxc(combo_operand=4,literal_operand = 4):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    B = B ^ C

def out(combo_operand=5,literal_operand = 5):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    return combo_operand % 8

def bdv(combo_operand=6,literal_operand = 6):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    B = A // (combo_operand**2)
    

def cdv(combo_operand=7,literal_operand = 7):
    global A,B,C,INSTRUCTION_POINTER
    INSTRUCTION_POINTER += 2
    C = A // (combo_operand**2)





def next_programstep(program) -> tuple[int]:
        global INSTRUCTION_POINTER
        instruction =  program[INSTRUCTION_POINTER]
        operant = program[INSTRUCTION_POINTER+1]
        match (operant):
            case 0,1,2,3:
                operant = operant
            case 4:
                operant = A
            case 5:
                operant = B
            case 6:
                operant = C   
            case 7, _:
                raise Exception("unvalide combo operant")
        return instruction,operant



def start_program(program,register_A,register_B,register_C):
    global A,B,C,INSTRUCTION_POINTER
    # initialize registers
    INSTRUCTION_POINTER = 0
    A=register_A
    B=register_B
    C=register_C
    # run the program
    program = list(map(int,program.split(',')))
    return run_program(program=program)


# run programm
def run_program(program = ""):
    global INSTRUCTION_POINTER

    output_values = []
    while INSTRUCTION_POINTER < len(program):
        instruction,operant = next_programstep(program)
        print(f"{instruction=}")
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




# Example usage:
register_a = 729
register_b = 0
register_c = 0
program = "0,1,5,4,3,0"

output = start_program(program,register_a,register_b,register_c)
print(output)  # Expected output: "4,6,3,5,6,3,5,2,1,0"
