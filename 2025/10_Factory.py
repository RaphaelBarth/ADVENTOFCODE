from functools import reduce
from itertools import combinations
import re
from timeit import default_timer as timer

import z3 as z3

from aoc_utils.aoc import AoC

# initialize AoC instance and read data
aoc = AoC(day=10, year=2025, use_example=False)

machine_manuals = []
# process each line to extract machine components 
for lines in aoc.get_stream().readlines():
    # extract single indicator light diagram, button wiring schematics, and joltage requirements using a single regex
    match = re.search(r'\[([.#]+)\].*?\(([\d,)]+)\).*?\{([\d,]+)\}', lines)
    if match:
        single_indicator_light_diagram = list(match.group(1))
        button_wiring_schematics = [tuple(map(int, m.split(','))) for m in re.findall(r'\(([\d,]+)\)', lines)]
        joltage_requirements = tuple(map(int, match.group(3).split(',')))

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


# start PART 2
timestamp1 = timer()

button_presses_needed = []
# process each machine manual to determine button presses needed
for machine in machine_manuals:
    # determine target value from joltage requirements
    target = machine["joltage_requirements"]
    buttons = machine["button_wiring_schematics"]

    # Create Z3 solver
    optimizer = z3.Optimize()

    # Create integer variables for each button (number of times pressed)
    button_vars = [z3.Int(f'b{i}') for i in range(len(buttons))]

    # Add constraints: each button press count must be non-negative and integer
    [optimizer.add(var >= 0) for var in button_vars]
        
    # Add constraints for each joltage requirement
    for idx, target_val in enumerate(target):
        # Sum of button presses that affect this joltage position
        constraint = z3.Sum([button_vars[j] for j in range(len(buttons)) if idx in buttons[j]]) == target_val
        optimizer.add(constraint)
    
    # Minimize total button presses
    model = optimizer.minimize(z3.Sum(button_vars))  
    optimizer.check()
    # extract the model (solution) and record the total button presses needed
    button_presses_needed.append(model.lower().as_string())
     
        
print(f"PART2: {sum( map(int, button_presses_needed))=} in {(timestamp2:=timer())-timestamp1}sec")