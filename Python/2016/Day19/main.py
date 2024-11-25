
num_elves = int(open(0).read().strip())

class LinkedList:
    def __init__(self, num):
        self.index = num
        self.next = None
        self.prev = None

    def take_presents(self):
        self.next.next.prev = self
        self.next = self.next.next

    def __repr__(self):
        return f"Elf {self.index} -> Prev: {self.prev.index}, Next: {self.next.index}"

def part1():
    start = LinkedList(1)
    curr = start

    for i in range(num_elves - 1):
        node = LinkedList(i + 2)
        curr.next = node
        node.prev = curr
        curr = node

    curr.next = start
    start.prev = curr

    curr = start

    while curr.next != curr:
        curr.take_presents()
        curr = curr.next

    return curr.index

print("Part 1:", part1())



















