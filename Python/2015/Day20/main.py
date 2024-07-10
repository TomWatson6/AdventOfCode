
from collections import defaultdict
import math

input = 34000000
E = defaultdict(int)

def get_factors(number):
    factors = []
    sqrt_num = int(math.sqrt(number))
    
    for i in range(1, sqrt_num + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    
    return factors

def presents(house_number):
    factors = get_factors(house_number)
    output = 0

    for f in factors:
        output += f * 10

    return output

def presents2(house_number):
    global E
    factors = get_factors(house_number)
    output = 0

    for f in factors:
        if E[f] >= 50:
            continue
        E[f] += 1
        output += f * 11

    return output


def search(number):
    for i in range(1, number):
        outcome = presents(i)
        if outcome > number:
            return i

def search2(number):
    for i in range(1, number):
        outcome = presents2(i)
        if outcome > number:
            return i
    
print("Part 1:", search(input))
print("Part 2:", search2(input))





