from collections import defaultdict

lower = 97
upper = 122

class Room:
    def __init__(self, input):
        self.checksum = input[1]
        parts = input[0].split("-")
        self.sector_id = int(parts[-1])
        parts = parts[:-1]
        self.raw = " ".join(parts)
        parts = [x for sublist in parts for x in sublist]
        self.letters = parts

    def count_letters(self):
        frequencies = defaultdict(lambda: 0)

        for x in self.letters:
            frequencies[x] += 1

        return frequencies

    def get_most_common(self):
        frequencies = self.count_letters()

        frequencies = sorted(frequencies.items(), key=lambda v: v[1], reverse=True)

        return {x[0]: x[1] for x in frequencies}

    def decipher(self):
        output = ""

        for c in self.raw:
            if c != " ":
                o = ord(c)
                o -= lower
                o += self.sector_id
                o %= upper - lower + 1
                o += lower
                output += chr(o)
            else:
                output += c

        return output


with open("input.txt") as f:
    input = [[y.strip("]") for y in x.strip().split("[")] for x in f.readlines()]

rooms = [Room(x) for x in input]
valid_rooms = []

for room in rooms:
    most_common = room.get_most_common()
    valid = True

    for c in room.checksum:
        curr = most_common.get(c)
        if curr != None:
            for v in most_common.values():
                if curr < v:
                    valid = False
                    break
            del most_common[c]
            if not valid:
               break 
        else:
            valid = False
            break
    if valid:
        valid_rooms.append(room)

print("Part 1: {}".format(sum([x.sector_id for x in valid_rooms])))

deciphered = []

for x in rooms:
    deciphered.append((x.sector_id, x.decipher()))

deciphered = [x for x in deciphered if "north" in x[1]]

print("Part 2: {}".format(deciphered[0][0]))
