
class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.curr = None
        self.length = 0

    def add(self, value):
        node = Node(value, self.curr, self.curr.next)
        self.curr.next.prev = node
        self.curr.next = node
        self.curr = node
        self.length += 1

    def delete(self):
        self.curr.prev.next = self.curr.next
        self.curr.next.prev = self.curr.prev
        self.curr = self.curr.next
        self.length -= 1

    def forward(self, count):
        for _ in range(count):
            self.curr = self.curr.next

    def backward(self, count):
        for _ in range(count):
            self.curr = self.curr.prev

players = 486
final_score = 70833

N = DoublyLinkedList()
P = [0 for _ in range(players)]
curr = 0

while True:
    if curr == 0:
        N.curr = Node(curr, None, None)
        N.curr.next = N.curr
        N.curr.prev = N.curr
        N.length = 1
    elif curr % 23 != 0:
        N.add(curr)

    if curr % 23 == 0 and curr != 0:
        P[curr % len(P)] += curr
        N.backward(8)
        P[curr % len(P)] += N.curr.value
        N.delete()
        N.forward(1)
        curr += 1
        continue

    curr += 1
    N.forward(1)

    if curr == final_score:
        print("Part 1:", max(P))

    if curr == final_score * 100:
        break

print("Part 2:", max(P))
















