
input = 170641
# input = 51589
last = 0
count = 0
latest = ""

linked_list = []
seen = False

class LinkedList:
    def __init__(self, val, next):
        self.val = val
        self.next = next
        
        global last, count, linked_list
        last = self
        count += 1
        linked_list.append(self)
        if len(linked_list) > len(str(input)):
            global latest, seen
            latest = "".join([str(x.val) for x in linked_list[len(linked_list) - len(str(input)):len(linked_list)]])
            if latest == str(input):
                seen = True
                print("seen at: " + str(count - len(str(input))))
            # print(latest)

l1 = LinkedList(3, 0)
first = l1
l2 = LinkedList(7, l1)
l1.next = l2

elves = [l1, l2]

def add_recipe():
    sum = 0
    global elves
    for i in range(len(elves)):
        sum += elves[i].val

    for num in [int(x) for x in str(sum)]:
        curr = last
        curr.next = LinkedList(num, first)

    for i in range(len(elves)):
        for _ in range(elves[i].val + 1):
            elves[i] = elves[i].next

while count < input + 10 or not seen:
    add_recipe()

# print("".join([str(x.val) for x in linked_list]))

output = "".join([str(x.val) for x in linked_list[input:input+10]])

print(f"Part 1: {output}")

print(f"Part 2: {count - len(str(input)) - 1}")

























