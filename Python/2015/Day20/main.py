
input = 34000000
houses = []
counters = []
counter = 1

def get_factors(x):
    factors = []

    for i in range(1, x + 1):
        if x % i == 0 and i % 10 == 0:
            factors.append(i)
            
    return factors


factors = get_factors(input)
combinations = []



# def get_numbers(numbers, curr, amount):
#     if amount == 0:
#         return None

#     combos = []

#     for n in numbers:
#         if amount > 1:
#             temp = get_numbers([x for x in numbers if x != n], [n], amount - 1)
#             temp.append(n)
#             [combos.append(t) for t in temp]
#         elif amount == 1:
#             combos.append(n)

#     return list(set(combos))


# print(get_numbers(factors, 2))


# print(f"Part 1: {}")





