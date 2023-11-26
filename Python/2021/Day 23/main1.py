

class Maze:
    def __init__(self, input):
        input = [x for x in [y for y in input]]
        self.grid = {}
        for i, row in enumerate(input):
            for j, val in enumerate(row):
                self.grid[(j, i)] = val
        self.corr = 1 # The row that the corridor is on
        


COST = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

DESTINATION = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

corridor = [None for _ in range(11)]

A = ["D", "C"]
B = ["A", "A"]
C = ["D", "B"]
D = ["C", "B"]









