import functools
import itertools
from timeit import default_timer as timer


example= """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

with open("2024/Day23/data.txt") as file:
    data = file.read()
    #data = example

    all_connections = {}
    for connection in map(lambda line :line.split('-'),data.split()):
        computer_0 ,computer_1 = connection[0], connection[1]
        all_connections[computer_0] = all_connections.get(computer_0,set()) | {computer_1} 
        all_connections[computer_1] = all_connections.get(computer_1,set()) | {computer_0}

    timestamp = timer()
    sets_of_three_computers = set()
    for computer, connections in all_connections.items():   
        matches = filter(lambda ele: ele[0] in all_connections[ele[1]],itertools.combinations(connections,2))
        sets_of_three_computers.update(map(tuple,map(lambda ele: sorted([ele[0],ele[1],computer]),matches)))
    sets_of_three_computers = set(filter(lambda ele:any(s.startswith('t') for s in ele)  ,sets_of_three_computers))

    print(f"PART1: {len(sets_of_three_computers)=} in {(timer())-timestamp}sec")
    
    timestamp = timer()

    @functools.cache
    def fun (computers : frozenset,intersection : frozenset):
        if not intersection:
            return computers
        
        temp = computers
        for computer in intersection:
            new_computers = frozenset({computer} | computers)
            new_intersection = frozenset.intersection(intersection,all_connections[computer])
            temp = max(temp,fun(new_computers,intersection=new_intersection),key=len)

        return temp

    sets_of_computers = set()
    for computer, connections in all_connections.items():
        computer,connections = frozenset({computer}), frozenset(connections)
        sets_of_computers = max(fun(computer,connections),sets_of_computers,key=len)
    
    result_str = ','.join(sorted(sets_of_computers))
    print(f"PART2: {result_str=} in {(timer())-timestamp}sec")

   
  

            
            

    