from functools import reduce
from itertools import combinations, combinations_with_replacement
import re
import sys
from timeit import default_timer as timer
from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aco = AoC(day=10, year=2025, use_example=False)
data = aco.DATA

machine_manuals = []
# process each line to extract machine components 
for lines in data.splitlines():
    # extract single indicator light diagram
    temp_matches = re.findall(r'\[([.#]+)\]', lines)
    single_indicator_light_diagram  = list(temp_matches[0])
    # extract button wiring schematics and convert to list of tuples
    temp_matches = re.findall(r'\(([\d,]+)\)', lines)
    button_wiring_schematics = [tuple(map(int,match.split(','))) for match in temp_matches]
    # extract joltage requirements and convert to tuple of integers
    temp_matches = re.findall(r'\{([\d,]+)\}', lines)[0]
    joltage_requirements = tuple(map(int,temp_matches.split(',')))

    # assemble machine manual
    machine = {"single_indicator_light_diagram": single_indicator_light_diagram,
               "button_wiring_schematics": button_wiring_schematics,
               "joltage_requirements":  joltage_requirements}
    # add machine manual to list
    machine_manuals.append(machine)

# start PART 1
timestamp1 = timer()

button_presses_needed = []
# process each machine manual to determine button presses needed
for machine in machine_manuals:
    # determine target value from light diagram by interpreting '#' as 1 and '.' as 0 in  reversed binary (e.g. '.#..#' -> 10010 -> 18)
    target = int(''.join('1' if c == '#' else '0' for c in reversed(machine["single_indicator_light_diagram"])), 2)
    # create list of button values by interpreting each button wiring schematic as a binary number e.g. (0,3) -> 1001 -> 9
    buttons = [sum(1 << pos for pos in button) for button in machine["button_wiring_schematics"]]

    idx = 1
    found = False
    # find the minimum number of button presses needed to reach the target value using combinations of button values
    while not found:
        # check all combinations of buttons of length idx
        for combo in combinations(buttons, idx):
            # calculate the xor value of the combination
            val = reduce(lambda a,b: a ^ b, combo,0)
            # check if the calculated value matches the target
            if target == val:
                # record the number of button presses needed, mark as found and continue to next machine
                button_presses_needed.append(idx)
                found = True
                break
        # increment the combination length if no match was found
        idx += 1


print(f"PART1: {sum(button_presses_needed)=} in {(timestamp2:=timer())-timestamp1}sec")





# start PART 1
timestamp1 = timer()

button_presses_needed = []
# process each machine manual to determine button presses needed

for m_idx, machine in enumerate(machine_manuals):
    # determine target value from joltage requirements
    target = list(machine["joltage_requirements"])
    buttons = machine["button_wiring_schematics"]
    idx = 1

    found = False
    # find the minimum number of button presses needed to reach the target value using combinations of button values
    while not found:
        sys.stdout.write(f"\rmachine {m_idx+1}/{len(machine_manuals)} @ {idx=}")
        sys.stdout.flush()
        # check all combinations of buttons of length idx
        for combo in combinations_with_replacement(buttons, idx):
            # calculate the xor value of the combination
            current = len(target)*[0]
            for button in combo:
                for i in button:
                    current[i] += 1 
            
            if target == current:
                # record the number of button presses needed, mark as found and continue to next machine
                button_presses_needed.append(idx)
                found = True
                break
        # increment the combination length if no match was found
        idx += 1
        print()


print(f"PART2: {sum(button_presses_needed)=} in {(timestamp2:=timer())-timestamp1}sec")