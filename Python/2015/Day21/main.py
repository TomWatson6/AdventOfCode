

class Player:
    def __init__(self, items):
        self.health = 100
        self.damage = sum(items, key=lambda item: item.damage)
        self.armor = sum(items, key=lambda item: item.armor)
        self.cost = sum(items, key=lambda item: item.cost)

class Boss:
    def __init__(self, s):
        parts = [x.strip() for x in s.split("\n")]
        self.health = parts[0].split(" ")[2]
        self.damage = parts[1].split(" ")[1]
        self.armor = parts[2].split(" ")[1]

class Item:
    def __init__(self, s, t):
        parts = [x.strip().strip("+") for x in s.split(" ") if x != ""]
        self.name = parts[0]
        self.cost = int(parts[-3])
        self.damage = int(parts[-2])
        self.armor = int(parts[-1])
        self.type = t
        print(self)

    def __str__(self):
        return f"Type: {self.type}\n{self.name}:\nDamage: {self.damage}\nArmor: {self.armor}\nCost: {self.cost}"

def get_shop(file_name):
    weapons = []
    armors = []
    rings = []

    with open(file_name) as f:
        input = [[y for y in x.split("\n")[1:] if len(y) != 1] for x in f.read().split("\n\n")]

    # Weapons
    for weapon in input[0]:
        weapons.append(Item(weapon, "weapon"))

    # Armor
    for armor in input[1]:
        armors.append(Item(armor, "armor"))

    # Rings
    for ring in input[2]:
        rings.append(Item(ring, "ring"))

    return weapons, armor, rings

def get_perms(weapons, armor, rings):
    W = []
    WA = []
    WAR = []

    for w in weapons:
        W.append([w])

    for w in W:
        WA.append(w)

    for a in armor:
        for w in W:
            WA.append([w[0], a])

    for wa in WA:
        WAR.append(wa)

    for wa in WA:
        for r in rings:
            col = wa
            col.append(r)
            WAR.append(col)

    mul = []
    for i in range(len(rings) - 1):
        for j in range(i, len(rings)):
            mul.append([rings[i], rings[j]])

    print([(a.name, b.name) for a, b in mul])

    for m in mul:
        for wa in WA:
            col = [wa]
            [col.append(r for r in m)]
            WAR.append(col)

    return WAR

def play_game(player, boss):
    '''
        player with items
        boss from input
        returns outcome (win/loss) as bool
    '''

weapons, armor, rings = get_shop("shop.txt")
boss = ""

with open("input.txt") as f:
    boss = Boss(f.read())

p = get_perms(weapons, armor, rings)

print("hello, world!")


