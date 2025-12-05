from functools import reduce
from timeit import default_timer as timer
from aoc_utils.aoc import AoC

def prune(secet_number):
    return secet_number % 16777216

def mix(secet_number,value):
    return secet_number ^ value

def step1(secret_number):
    return prune(mix(secret_number,secret_number << 6))

def step2(secret_number):
    return prune(mix(secret_number,secret_number >> 5))

def step3(secret_number):
    return prune(mix(secret_number,secret_number << 11))

def new_secert_number(secet_number):
    return step3(step2(step1(secet_number)))

def new_n_secret_numbers(secret_number,n=2000):
    secret_numbers = [secret_number]
    temp = secret_number
    for _ in range(n-1):
        temp = new_secert_number(temp)
        secret_numbers.append(temp)
    return secret_numbers

aoc = AoC(day=22, year=2024, use_example=False)
secret_numbers = list(map(int,aoc.DATA.split()))

timestamp = timer()
secret_number_sum = sum(reduce(lambda x,y: new_secert_number(x),range(2000),secet_number) for secet_number in secret_numbers)
print(f"PART1: {secret_number_sum=} in {(timer())-timestamp}sec")

per_monkey = []
for secret_number in secret_numbers:
    prices = list(map(lambda x: x % 10,new_n_secret_numbers(secret_number,2000)))
    changes = [prices[idx] - prices[idx-1] for idx in range(1,len(prices))]
    sequences = [tuple(changes[i:i+4],) for i in range(len(changes)-3)]
    per_monkey.append({s:p for s,p in reversed(list(zip(sequences,prices[4:])))})


all_sequences = set()
for monkey in per_monkey:
    all_sequences.update(monkey.keys())

most_bananas = 0
for sequence in all_sequences:
    current_bananas = 0
    for monkey in per_monkey:
        current_bananas += monkey.get(sequence,0)
        
    most_bananas= max(most_bananas,current_bananas)

print(f"PART2: {most_bananas=} in {(timer())-timestamp}sec")



  

            
            

    