

M = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}

B = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2',
}

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

numbers = [enumerate(list(x)[::-1]) for x in lines]
numbers = [sum([M[x[1]] * 5**x[0] for x in y]) for y in numbers]
total = sum(numbers)

def snafu(number):
    digits = []
    total = lambda: sum([(5 ** (30 - x[0])) * x[1] for x in enumerate(digits)])
    for i in range(30, -1, -1):
        nums = []
        for j in range(-2, 3):
            nums.append(j * (5 ** i))
        num = min(nums, key=lambda k: abs(total() - number + k))
        digits.append(nums.index(num) - 2)

    output = "".join(B[x] for x in digits)

    return output.lstrip("0")

print(snafu(total))











