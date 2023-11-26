from copy import deepcopy

class Node:
    def __init__(self, number):
        self.prev = None
        self.next = None
        self.value = number

with open("simple_input.txt") as f:
    numbers = [int(x.strip()) for x in f.readlines()]

nodes = []

for n in numbers:
    nodes.append(Node(n))

for i in range(len(nodes)):
    nodes[i].next = nodes[(i + 1) % len(nodes)]
    nodes[i].prev = nodes[(i - 1) % len(nodes)]

n = nodes[0]
for i in range(len(nodes)):
    print(n.value, end = ", ")
    n = n.next
print()

for i, node in enumerate(nodes):
    curr = node
    for x in range(abs(node.value)):
        if node.value < 0:
            curr = curr.prev
        if node.value > 0:
            curr = curr.next

    # curr = destination node
    # node needs to be inserted at this location
    # node.prev.next = node.next
    node.prev.next = node.next
    # node.next.prev = node.prev
    node.next.prev = node.prev
    curr.next.prev = node
    node.next = curr.next
    curr.next = node
    node.prev = curr
    # node.prev = curr
    # node.prev = curr
    # # node.next = curr.next
    # node.next = curr.next
    # # curr.next = node
    # curr.next = node

    n = nodes[0]
    for i in range(len(nodes)):
        print(n.value, end = ", ")
        n = n.next
    print()

# starting_points = [x for x in nodes if x.value == 0]
# assert len(starting_points) == 1

# curr = deepcopy(starting_points[0])
# product = 1

# for _ in range(3):
#     for _ in range(1000):
#         curr = deepcopy(curr.next)
#     print(curr.value)
#     product *= curr.value

# n = nodes[0]
# for i in range(len(nodes)):
#     print(n.value, end = ", ")
#     n = n.next
# print()

print(product)



# index => (value, left_index, right_index)
# numbers = {}

# for i, line in enumerate(lines):
#     numbers[i] = (line, (i-1)%len(lines), (i+1)%len(lines))

# for i, number in initial:
#     dest = (i + number) % len(numbers)
#     n = deepcopy(i)
#     if dest > i:
#         while n != dest:
#             numbers[n] = numbers[(n + 1) % len(numbers)]
#             n = (n + 1) % len(numbers)
#     elif dest < i:
#         while n != dest:
#             numbers[n] = numbers[(n - 1) % len(numbers)]
#             n = (n - 1) % len(numbers)

#     numbers[dest] = number
#     print(numbers)
#     assert sorted(numbers) == sorted([x[1] for x in initial])














