import re
from collections import defaultdict as dd
import itertools

class Rule:
    def __init__(self, s):
        matches = re.search("gain [0-9]* ", s)
        if matches != None:
            match = matches[0]
            match = match.split(" ")
            self.happy = 1
            self.change = int(match[1])

        matches = re.search("lose [0-9]* ", s)
        if matches != None:
            match = matches[0]
            match = match.split(" ")
            self.happy = -1
            self.change = int(match[1])
        
        if re.search("gain", s) != None:
            self.gain = 1
        else:
            self.gain = -1
        
        parts = [x.strip(".") for x in s.split(" ")]
        self.self = parts[0]
        self.other = parts[-1]

    def __str__(self):
        return "{} -> {} - {} {}".format(self.self, self.other, "gains" if self.happy == 1 else "loses", self.change)

rules = dd(lambda: {})

def best_arrangement(people):
    permutations = list(itertools.permutations(people))
    changes = []

    for perm in permutations:
        change = 0
        for i, p in enumerate(perm):
            change += rules[p][perm[(i + 1) % len(perm)]]
            change += rules[p][perm[(i - 1) % len(perm)]]
        changes.append(change)

    return max(changes)



with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines() if x != ""]

for line in lines:
    rule = Rule(line)
    rules[rule.self][rule.other] = rule.happy * rule.change

people = [x for x in rules.keys()]
change = best_arrangement(people)

print("Part 1: {}".format(change))

for p in people:
    rules["me"][p] = 0
    rules[p]["me"] = 0

people.append("me")
change = best_arrangement(people)

print("Part 2: {}".format(change))

