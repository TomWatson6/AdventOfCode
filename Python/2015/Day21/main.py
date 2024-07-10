from copy import deepcopy

class Player:
    def __init__(self, items):
        self.health = 100
        self.damage = sum([i.damage for i in items])
        self.armor = sum([i.armor for i in items])
        self.cost = sum([i.cost for i in items])

class Boss:
    def __init__(self, s):
        parts = [x.strip() for x in s.split("\n")]
        self.health = int(parts[0].split(" ")[2])
        self.damage = int(parts[1].split(" ")[1])
        self.armor = int(parts[2].split(" ")[1])

class Item:
    def __init__(self, s, t):
        parts = [x.strip().strip("+") for x in s.split(" ") if x != ""]
        self.name = parts[0]
        self.cost = int(parts[-3])
        self.damage = int(parts[-2])
        self.armor = int(parts[-1])
        self.type = t

    def __str__(self):
        return f"Type: {self.type}\nName: {self.name}\nDamage: {self.damage}\nArmor: {self.armor}\nCost: {self.cost}"

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

    return weapons, armors, rings

def get_perms(weapons, armor, rings):
    WA = [[w] for w in weapons] + [[w] + [a] for w in weapons for a in armor]
    R = []

    for a in range(len(rings) - 1):
        for b in range(a + 1, len(rings)):
            R.append([rings[a], rings[b]])

    # WA is no rings, rings has 1 rings, R has 2 rings to make all permutations
    WAR = WA + [wa + [r] for wa in WA for r in rings] + [wa + r for wa in WA for r in R]

    return WAR

def calc_damage(damage, armor):
    return max(1, damage - armor)

def play_game(player, boss):
    while True:
        boss.health -= calc_damage(player.damage, boss.armor)

        if boss.health <= 0:
            return True

        player.health -= calc_damage(boss.damage, player.armor)

        if player.health <= 0:
            return False

weapons, armor, rings = get_shop("shop.txt")
boss = ""

with open("input.txt") as f:
    boss = Boss(f.read())

perms = get_perms(weapons, armor, rings)
best = 1e9
worst = 0

for p in perms:
    player = Player(p)

    if play_game(player, deepcopy(boss)):
        best = min(best, player.cost)
    else:
        worst = max(worst, player.cost)

print("Part 1:", best)
print("Part 2:", worst)
