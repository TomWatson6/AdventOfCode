
class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.prev.val}, {self.next.val}"

class LinkedList:
    def __init__(self, items):
        self.root = Node(items[0])
        self.list = {}
        self.list[0] = self.root
        self.indices = [i for i in range(len(items))]
        prev = self.root

        for i, item in enumerate(items[1:]):
            n = Node(item, prev)
            self.list[i + 1] = n
            prev.next = n
            prev = n

        self.root.prev = n
        n.next = self.root

    def remove(self, n):
        self.list[(n - 1) % len(self.list)].next = self.list[n].next
        self.list[(n + 1) % len(self.list)].prev = self.list[n].prev
        self.indices.remove(n)
        # self.list = self.list[:n] + self.list[(n + 1) % len(self.list):]
        # self.list.pop(n)
        # self.list[n] = self.list[(n - 1) % len(self.list)]
    
input = open("input.txt").read().strip()

def parse(input: str):
    return int(input)

def part1(input: str) -> int:
    amount = parse(input)

    taken_from = set()

    i = 0
    take = False
    taking_elf = 0

    while len(taken_from) != amount - 1:
        if i % amount in taken_from:
            i += 1
            continue

        if take:
            taken_from.add(i % amount)
        else:
            taking_elf = i % amount

        take = not take
        i += 1

    return taking_elf + 1

def part2(input: str) -> int:
    target = parse(input)

    i = 1

    while i * 3 < target:
        i *= 3

    return target - i

    # elves = LinkedList([i for i in range(amount)])
    # curr = elves.root

    # while len(elves.indices) > 1:
    #     opp = (curr.val + len(elves.indices) // 2) % len(elves.indices)
    #     opp = elves.indices[opp]
    #     print(f"{curr=}, {opp=}, {len(elves.indices)=}, {elves.indices=}")
    #     elves.remove(opp)
    #     curr = curr.next

    # return curr.val + 1

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))















