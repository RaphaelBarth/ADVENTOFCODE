import re 
from aoc_utils.aoc import AoC

def apply_rules(rules,update:list) -> bool:
    for rule in rules:
        first,second = rule
        idx_first = update.index(first)  if first in update else None
        idx_second = update.index(second) if second in update else None

        #print(rule,(idx_first,idx_second))

        if idx_first is not None and idx_second is not None:
            if idx_first > idx_second:
                return False
            
    return True
        
def fix_update(rules,update:list): 
    while not apply_rules(rules,update): 
        for rule in rules:
            first,second = rule
            idx_first = update.index(first)  if first in update else None
            idx_second = update.index(second) if second in update else None

            #print(rule,(idx_first,idx_second))

            if idx_first is not None and idx_second is not None:
                if idx_first > idx_second:
                    update.insert(idx_first,update.pop(idx_second))
            
    return update

aoc = AoC(day=5, year=2024, use_example=False)

data = aoc.DATA
rules,queue = [],[]
#print(data)
for line in data.split():
    if re.match(r"\d+\|\d+",line):
        rules.append(tuple(line.split("|")))
    elif re.match(r"((\d+,)+\d+)",line):
        queue.append(line.split(","))
    else:
        pass
good,bad = [],[]
[good.append(update)  if apply_rules(rules,update) else bad.append(update) for update in queue]
    
print(sum([int(entry[len(entry)//2]) for entry in good]))

fixed_updates = map(lambda xx:fix_update(rules,xx),bad)
middle_page_number = map(lambda x : int(x[len(x)//2]),fixed_updates)
print(sum(middle_page_number))