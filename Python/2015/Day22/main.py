from copy import deepcopy
import re

class Player:
    def __init__(self):
        self.health = 50
        self.mana = 500
        self.armor = 0
        self.effects = [] # (name, turns)

    def apply_effects(self, boss):
        self.apply_non_effects()
        self.apply_active_effects(boss)

    def apply_non_effects(self):
        self.armor = 0

    def apply_active_effects(self, boss):
        new_effects = []
        for effect in self.effects:
            if effect[0] == "shield":
                self.armor = 7
            elif effect[0] == "poison":
                boss.health -= 3
            elif effect[0] == "recharge":
                self.mana += 101

            new_effect = (effect[0], effect[1] - 1)
            new_effects.append(new_effect)

        self.effects = [x for x in new_effects if x[1] > 0]

    def get_spells(self):
        return [
            (self.magic_missile, 53),
            (self.drain, 73),
            (self.shield, 113),
            (self.poison, 173),
            (self.recharge, 229),
        ]

    def magic_missile(self, boss):
        if self.mana < 53:
            return False

        self.mana -= 53
        boss.health -= 4
        return True

    def drain(self, boss):
        if self.mana < 73:
            return False

        self.mana -= 73
        boss.health -= 2
        self.health += 2
        return True

    def shield(self, boss):
        if self.mana < 113:
            return False

        if "shield" in [x[0] for x in self.effects]:
            return False

        self.mana -= 113
        self.effects.append(("shield", 6))
        return True

    def poison(self, boss):
        if self.mana < 173:
            return False

        if "poison" in [x[0] for x in self.effects]:
            return False

        self.mana -= 173
        self.effects.append(("poison", 6))
        return True

    def recharge(self, boss):
        if self.mana < 229:
            return False

        if "recharge" in [x[0] for x in self.effects]:
            return False

        self.mana -= 229
        self.effects.append(("recharge", 5))
        return True

    def __str__(self):
        return f"Player(health={self.health}, mana={self.mana}, armor={self.armor}, effects={self.effects})"

class Boss:
    def __init__(self, s):
        parts = [x.strip() for x in s.split("\n")]
        self.health = int(parts[0].split(" ")[2])
        self.damage = int(parts[1].split(" ")[1])

    def __str__(self):
        return f"Boss(health={self.health}, damage={self.damage})"

def calc_damage(damage, armor):
    return max(1, damage - armor)

lowest_mana = int(1e9)

def play_game(player, boss, mana_spent, turn, spells_cast, p2):
    global lowest_mana

    if mana_spent > lowest_mana:
        return

    if turn == 0:
        # Players Turn
        # Hard mode
        if p2:
            player.health -= 1
            if player.health <= 0:
                return

        ph, pm, pa, pe = player.health, player.mana, player.armor, player.effects
        bh, bd = boss.health, boss.damage

        for spell, cost in player.get_spells():
            player.health, player.mana, player.armor, player.effects = ph, pm, pa, deepcopy(pe)
            boss.health, boss.damage = bh, bd
            player.apply_effects(boss)

            if boss.health <= 0:
                lowest_mana = min(lowest_mana, mana_spent)
                return

            if not spell(boss):
                continue

            if boss.health <= 0:
                lowest_mana = min(lowest_mana, mana_spent + cost)
                continue

            play_game(player, boss, mana_spent + cost, 1, spells_cast + [spell.__name__], p2)

    else:
        # Bosses Turn
        player.apply_effects(boss)

        if boss.health <= 0:
            lowest_mana = min(lowest_mana, mana_spent)
            return

        player.health -= calc_damage(boss.damage, player.armor)

        if player.health <= 0:
            return

        play_game(player, boss, mana_spent, 0, spells_cast, p2)


boss = ""

with open(0) as f:
    boss = Boss(f.read())

c_boss = deepcopy(boss)

player = Player()

play_game(player, boss, 0, 0, [], False)

print("Part 1:", lowest_mana)

lowest_mana = int(1e9)
player = Player()
boss = deepcopy(c_boss)

play_game(player, boss, 0, 0, [], True)

print("Part 2:", lowest_mana)

