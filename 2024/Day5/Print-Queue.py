import re 
from functools import reduce
temp = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

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


with open("2024/Day5/data.txt") as file:
    data = file.read()
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