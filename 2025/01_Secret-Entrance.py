from timeit import default_timer as timer

EXAMPLE = False
if EXAMPLE: 
    document ="""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
else:
    with open("2025/Day1/data.txt") as f:
        document = f.read().strip()


MAX_DIAL_NUMBER = 99

timestamp1 = timer()
dial_position = 50
dial_zeroed = 0
# split the instructions by line
for instruction in document.split("\n"):
    direction, steps = instruction[0], int(instruction[1:])

    # rotate the dial by the given steps
    dial_position = (dial_position - steps if direction == "L" else dial_position + steps) % (MAX_DIAL_NUMBER + 1) 
    
    # check if the dial is at zero and increment the counter
    dial_zeroed += 1 if dial_position == 0 else 0

print(f"PART1: {dial_zeroed=} in {(timestamp2:=timer())-timestamp1}sec")



timestamp1 = timer()
dial_position = 50
dial_zeroed = 0
is_zero = False

# split the instructions by line
for instruction in document.split("\n"):
    direction, steps = instruction[0], int(instruction[1:])

    # check if the dial is at zero before rotation
    is_zero = True if dial_position == 0 else False

    # rotate the dial by the given steps
    dial_position = (dial_position - steps if direction == "L" else dial_position + steps) 

    # check if the dial crossed zero or is at zero and increment the counter
    if dial_position < 0 and not is_zero or not dial_position:
        dial_zeroed += 1

    # add the number of times the dial has crossed zero
    dial_zeroed += int(abs(dial_position) / (MAX_DIAL_NUMBER+1)) 

    # finally, wrap the dial position within the valid range
    dial_position = dial_position % (MAX_DIAL_NUMBER + 1)

print(f"PART2: {dial_zeroed=} in {(timestamp2:=timer())-timestamp1}sec")