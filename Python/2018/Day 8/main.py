
class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def size(self):
        total = 0

        for c in self.children:
            total += c.size()

        return total + sum(self.metadata)

    def p2_size(self):
        if len(self.children) > 0:
            total = 0
            for m in self.metadata:
                if m - 1 < len(self.children):
                    total += self.children[m - 1].p2_size()
            
            return total

        return sum(self.metadata)

with open("input.txt") as f:
    numbers = list(map(int, f.read().strip().split()))

# STATE
# 0 - read child
# 1 - read metadata

def create(numbers, index, state):
    curr = Node()
    if state == 1:
        return numbers[index], index + 1

    children, meta = numbers[index], numbers[index + 1]

    index += 2

    for c in range(children):
        child, index = create(numbers, index, 0)
        curr.children.append(child)
    for m in range(meta):
        metadata, index = create(numbers, index, 1)
        curr.metadata.append(metadata)

    return curr, index

root = create(numbers, 0, 0)[0]

print("Part 1:", root.size())
print("Part 2:", root.p2_size())















