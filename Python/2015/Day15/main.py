import itertools

class Ingredient:
    def __init__(self, s):
        parts = s.split(" ")
        self.name = parts[0].strip(":")
        self.capacity = int(parts[2].strip(","))
        self.durability = int(parts[4].strip(","))
        self.flavor = int(parts[6].strip(","))
        self.texture = int(parts[8].strip(","))
        self.calories = int(parts[10].strip(","))

    def value(self, i, x):
        if i == 0:
            return self.capacity * x
        elif i == 1:
            return self.durability * x
        elif i == 2:
            return self.flavor * x
        elif i == 3:
            return self.texture * x
        else:
            return self.calories * x

    # def cap_value(self, x):
    #     v = self.capacity * x
    #     return v

    # def dur_value(self, x):
    #     v = self.durability * x
    #     return v

    # def flavor_value(self, x):
    #     v = self.flavor * x
    #     return v

    # def texture_value(self, x):
    #     v = self.texture * x
    #     return v

    # def calorie_value(self, x):
    #     v = self.calories * x
    #     return v


with open("input.txt") as f:
    ingreds = [Ingredient(x) for x in f.readlines() if x != ""]

combos = []

for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            for d in range(1, 100):
                if a + b + c + d == 100:
                    combos.append([a, b, c, d])

perms = {}

for c in combos:
    p = itertools.permutations(c)
    for p0 in p:
        perms[tuple(p0)] = True

perms = [list(x) for x in perms.keys()]

print("Generated {} perms to run through".format(len(perms)))

max_calories = 500
cal_highest = 0
highest = 0

for p in perms:
    values = []

    for i in range(5):
        value = 0
        for j in range(4):
            value += ingreds[j].value(i, p[j])
        values.append(value)

    for i in range(len(values)):
        if values[i] < 0:
            values[i] = 0

    v = values[0] * values[1] * values[2] * values[3]
    highest = max(highest, v)
    if values[4] == max_calories:
        cal_highest = max(cal_highest, v)

print("Part 1: {}".format(highest))
print("Part 2: {}".format(cal_highest))


