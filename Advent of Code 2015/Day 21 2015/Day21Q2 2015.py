"""
Author:     Brian Mascitello
Date:       12/9/2018
Websites:   https://adventofcode.com/2015/day/21
Info:       --- Day 21: RPG Simulator 20XX ---
            --- Part Two ---
"""


class Unit:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return_str = '{0} Data: {1} hp, {2} damage, {3} armor.'

        return return_str.format(self.name, self.hp, self.damage, self.armor)

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_damage(self):
        return self.damage

    def get_armor(self):
        return self.armor

    def take_damage(self, attack):
        if self.name == 'boss':
            return_str = '- The player deals {0}-{1} = {2} damage; the boss goes down to {3} hit points.'
        else:
            return_str = '- The boss deals {0}-{1} = {2} damage; the player goes down to {3} hit points.'

        actual_damage = attack - self.armor

        if actual_damage < 1:
            actual_damage = 1

        self.hp -= actual_damage

        return return_str.format(attack, self.armor, actual_damage, self.hp)


class Item:
    def __init__(self, type, name, cost, damage, armor):
        self.type = type
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return_str = 'Item Data: {0}, {1}, {2} cost, {3} damage, {4} armor.'

        return return_str.format(self.type, self.name, self.cost, self.damage, self.armor)


def fight(player1, enemy1):
    """Returns True if the player wins."""

    while player1.get_hp() > 0 and enemy1.get_hp() > 0:
        # enemy1 takes damage first
        enemy1.take_damage(player1.get_damage())

        # if enemy1 faints, return True as player1 wins
        if enemy1.get_hp() < 1:
            return True

        # player1 takes damage second if enemy1 survives
        player1.take_damage(enemy1.get_damage())

        # player1 loses if it faints
        if player1.get_hp() < 1:
            return False


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


# Create Boss
data = get_data('Day21Q1 2015 Boss.txt')

boss_data = list()
for line in data.splitlines():
    boss_data.append(int(line.split()[-1]))

# boss = Unit('boss', boss_data[0], boss_data[1], boss_data[2])

# Create Shop
data = get_data('Day21Q1 2015 Shop.txt')
shop_data = list()
item_list = list()
item_type = ''
for line in data.splitlines():
    if len(line) != 0:
        # Checks to see if row is type header, reassigns type.
        if 'Weapon' in line.split()[0]:
            item_type = 'Weapon'
            continue
        elif 'Armor' in line.split()[0]:
            item_type = 'Armor'
            continue
        elif 'Ring' in line.split()[0]:
            item_type = 'Ring'
            continue

        if item_type != 'Ring':
            name = line.split()[0]
            cost = int(line.split()[1])
            damage = int(line.split()[2])
            armor = int(line.split()[3])
        else:
            name = line.split()[0] + ' ' + line.split()[1]
            cost = int(line.split()[2])
            damage = int(line.split()[3])
            armor = int(line.split()[4])

        new_item = Item(item_type, name, cost, damage, armor)

        item_list.append(new_item)

weapons = list()
armors = list()
rings = list()
for item in item_list:
    if item.type == 'Weapon':
        weapons.append(item)
    elif item.type == 'Armor':
        armors.append(item)
    else:
        rings.append(item)

all_combinations = list()

# Weapons
for w in weapons:
    all_combinations.append([w])

# Weapons and Armor
for w in weapons:
    for a in armors:
        all_combinations.append([w, a])

# Weapons and 1 Ring
for w in weapons:
    for r in rings:
        all_combinations.append([w, r])

# Weapons and Armor and 1 Ring
for w in weapons:
    for a in armors:
        for r in rings:
            all_combinations.append([w, a, r])

# Weapons and 2 Rings
for w in weapons:
    for r in rings:
        for x in rings:

            # Check to see if rings are different before adding.
            if r != x:

                # Check to see if combo is already in combinations.
                if [w, x, r] not in all_combinations:
                    all_combinations.append([w, r, x])

# Weapons and Armor and 2 Rings
for w in weapons:
    for a in armors:
        for r in rings:
            for x in rings:

                # Check to see if rings are different before adding.
                if r != x:

                    # Check to see if combo is already in combinations.
                    if [w, a, x, r] not in all_combinations:
                        all_combinations.append([w, a, r, x])

failure = []
success = []
# Calculate sum of all items per combo, create a player with those stats and test.
for combo in all_combinations:
    item_names = list()
    total_cost = 0
    total_damage = 0
    total_armor = 0

    for item_sets in combo:
        # print(item_sets)

        item_names.append(item_sets.name)
        total_cost += item_sets.cost
        total_damage += item_sets.damage
        total_armor += item_sets.armor

    # print(total_cost, item_names, total_damage, total_armor)

    player = Unit('player', 100, total_damage, total_armor)
    boss = Unit('boss', boss_data[0], boss_data[1], boss_data[2])

    fight_results = fight(player, boss)

    if fight_results:
        success.append(total_cost)
    else:
        failure.append(total_cost)

cheapest = sorted(success)[0]
print('The cheapest build cost is {0}.'.format(cheapest))

most_expensive = sorted(failure)[-1]
print('The most expensive build cost is {0}.'.format(most_expensive))

# The cheapest build cost is 111.
# The most expensive build cost is 188.
