

class Board:
    def __init__(self, lines):
        self.numbers = dict()
        self.marked = []
        self.dimensions = len(lines)
        self.winner = False
        
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                self.numbers[int(lines[x][y])] = [x, y]

    def mark(self, number):
        if number in self.numbers.keys():
            if self.numbers[number] not in self.marked:
                self.marked.append(self.numbers[number])

    def is_winner(self):
        if self.winner:
            return False

        for x in range(self.dimensions):
            slice = [a for a in self.marked if a[0] == x]
            if len(slice) == self.dimensions:
                self.winner = True
                return True
        for y in range(self.dimensions):
            slice = [a for a in self.marked if a[1] == y]
            if len(slice) == self.dimensions:
                self.winner = True
                return True
        return False
    
    def get_remaining(self):
        remaining = []

        for k, v in self.numbers.items():
            if v not in self.marked:
                remaining.append(k)

        return remaining