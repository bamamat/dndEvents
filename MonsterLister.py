import random
import webbrowser


def monsterParser(file):
    f = open(file, "r")
    file_contents = f.read()
    name = []
    name_list = []
    cr = []
    cr_list = []
    counter = 0
    prev_letter = ''

    for letter in file_contents:
        if letter == '\t':
            if prev_letter != '\t':
                counter += 1
        elif letter == '\n':
            counter = 0
            name_list.append(''.join(name))
            cr_list.append(''.join(cr))
            name = []
            cr = []
        elif counter == 0:
            name.append(letter)
        elif counter == 4:
            if letter == 'L' or letter == 'N' or letter == 'C' or letter == 'U' or letter == 'A':
                counter -= 1
            else:
                cr.append(letter)
        else:
            pass
        prev_letter = letter
    return name_list, cr_list


def randomShop():

    rare_dict = {0: 'common', 1: 'uncommon', 2: 'rare', 3: 'very rare', 4: 'legendary'}
    shop_dict = {0: 'blacksmith', 1: 'wand maker', 2: 'enchanter', 3: 'alchemist'}
    min_rarity = random.randint(0,4)
    max_rarity = random.randint(0,4)
    if min_rarity > max_rarity:
        temp = min_rarity
        min_rarity = max_rarity
        max_rarity = temp
    shop_type = random.randint(0,3)
    if shop_dict[shop_type] == 'enchanter' or shop_dict[shop_type] == 'alchemist':
        article = 'an '
    else:
        article = 'a '
    if min_rarity == max_rarity:
        print('you find ' + article + shop_dict[shop_type] + ' with ' + rare_dict[max_rarity] + ' items')
    else:
        print('you find ' + article + shop_dict[shop_type] + ' with ' + rare_dict[min_rarity] + ' to ' + rare_dict[
            max_rarity] + ' items')
    return [2, shop_dict[shop_type], rare_dict[min_rarity], rare_dict[max_rarity]]


def randomLoot(level):
    common_chance = -abs(level-1)+16
    uncommon_chance = -abs(level-5)+16
    rare_chance = -abs(level-9)+16
    very_rare_chance = -abs(level-13)+16
    legendary_chance = -abs(level-17)+16
    total = common_chance + uncommon_chance + rare_chance + very_rare_chance + legendary_chance
    loot = random.randint(1, total)
    if loot < common_chance:
        temp = 'Common'
    elif loot < common_chance + uncommon_chance:
        temp = 'Uncommon'
    elif loot < common_chance + uncommon_chance + rare_chance:
        temp = 'Rare'
    elif loot < common_chance + uncommon_chance + rare_chance + very_rare_chance:
        temp = 'Very Rare'
    else:
        temp = 'Legendary'

    roll = random.randint(1, 10)
    print(temp + ' loot')
    return [1, temp, roll]


def boringEvent():
    print("nothing exciting happens")
    return [3]


def randomDungeon():
    print("you find a hidden dungeon")
    return [4]


def randomEncounter(party_size, party_level, monsters, monsters_cr):
    xp_by_cr = {
        '0': 10, '1/8': 25, '1/4': 50, '1/2': 100,
        '1': 200, '2': 450, '3': 700, '4': 1100,
        '5': 1800, '6': 2300, '7': 2900, '8': 3900,
        '9': 5000, '10': 5900, '11': 7200, '12': 8400,
        '13': 10000, '14': 11500, '15': 13000, '16': 15000,
        '17': 18000, '18': 20000, '19': 22000, '20': 25000,
    }

    if party_size == 4:
        encounters = [
            [[5, 14], [3, 7], [2, 4], [1, 2], [1], [1], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
             []],
            [[8, 20], [4, 11], [3, 7], [2, 4], [1, 2], [1], [1], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
             [], []],
            [[11, 20], [6, 16], [3, 11], [2, 7], [2, 4], [1, 2], [1], [1], [1], [], [], [], [], [], [], [], [], [], [],
             [], [], [], []],
            [[15, 20], [8, 20], [5, 14], [3, 8], [2, 5], [2], [1, 2], [1], [1], [1], [], [], [], [], [], [], [], [], [],
             [], [], [], []],
            [[], [14, 20], [8, 20], [5, 14], [3, 9], [2, 5], [2, 4], [1, 2], [1, 2], [1], [1], [1], [1], [], [], [], [],
             [], [], [], [], [], []],
            [[], [15, 20], [10, 20], [6, 15], [3, 11], [2, 6], [2, 4], [2, 3], [1, 2], [1, 2], [1], [1], [1], [1], [1],
             [], [], [], [], [], [], [], []],
            [[], [15, 20], [11, 20], [7, 17], [4, 12], [3, 7], [2, 5], [2, 4], [1, 2], [1, 2], [1, 2], [1], [1], [1],
             [1], [1], [], [], [], [], [], [], []],
            [[], [18, 20], [12, 20], [8, 20], [5, 14], [3, 8], [2, 6], [2, 4], [1, 3], [1, 2], [1, 2], [1], [1], [1],
             [1], [1], [1], [], [], [], [], [], []],
            [[], [15, 20], [9, 20], [6, 15], [3, 9], [3, 7], [2, 5], [2, 3], [1, 2], [1, 2], [1, 2], [1], [1], [1], [1],
             [1], [1], [], [], [], [], [], []],
            [[], [15, 20], [10, 20], [6, 15], [3, 10], [3, 7], [2, 6], [2, 4], [2, 3], [1, 2], [1, 2], [1], [1], [1],
             [1], [1], [1], [1], [], [], [], [], []],
            [[], [16, 20], [11, 20], [7, 18], [4, 11], [3, 9], [2, 6], [2, 4], [2, 4], [2, 3], [1, 2], [1, 2], [1, 2],
             [1], [1], [1], [1], [1], [1], [1], [], [], []],
            [[], [20], [14, 20], [8, 20], [5, 14], [3, 11], [3, 7], [2, 5], [2, 4], [2, 4], [2], [1, 2], [1, 2], [1, 2],
             [1], [1], [1], [1], [1], [1], [1], [1], []],
            [[], [], [15, 20], [9, 20], [5, 14], [4, 11], [3, 8], [2, 6], [2, 5], [2, 4], [2, 3], [1, 2], [1, 2],
             [1, 2], [1, 2], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[], [], [15, 20], [10, 20], [6, 15], [4, 11], [3, 9], [2, 6], [2, 5], [2, 4], [2, 3], [1, 2], [1, 2],
             [1, 2], [1, 2], [1], [1], [1], [1], [1], [1], [1], [1]],
            [[], [], [15, 20], [11, 20], [7, 15], [4, 13], [3, 10], [3, 7], [2, 6], [2, 5], [2, 4], [2, 3], [1, 2],
             [1, 2], [1, 2], [1, 2], [1], [1], [1], [1], [1], [1], [1]],
            [[], [], [16, 20], [11, 20], [7, 16], [5, 14], [3, 11], [3, 7], [2, 6], [2, 5], [2, 4], [2, 3], [2, 3],
             [1, 2], [1, 2], [1, 2], [1, 2], [1], [1], [1], [1], [1], [1]],
            [[], [], [20], [14, 20], [8, 20], [6, 15], [4, 11], [3, 8], [3, 7], [2, 6], [2, 5], [2, 4], [2, 3], [2, 3],
             [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1], [1], [1], [1]],
            [[], [], [], [14, 20], [8, 20], [6, 15], [4, 12], [3, 9], [3, 7], [2, 6], [2, 5], [2, 4], [2, 4], [2, 3],
             [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1], [1], [1], [1]],
            [[], [], [], [15, 20], [9, 20], [7, 16], [5, 14], [3, 10], [3, 8], [3, 7], [2, 6], [2, 5], [2, 4], [2, 3],
             [2, 3], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1], [1], [1]],
            [[], [], [], [15, 20], [10, 20], [7, 19], [6, 15], [4, 11], [3, 9], [3, 8], [2, 6], [2, 6], [2, 5], [2, 4],
             [2, 3], [2, 3], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1]],
        ]

    cr_dict = {'0': 0, '1/8': 1, '1/4': 2, '1/2': 3}
    temp = {str(x): x + 3 for x in range(1, 20)}
    cr_dict.update(temp)

    cr = random.choice(list(cr_dict.items()))[0]
    monster_range = encounters[party_level - 1][cr_dict[cr]]
    while not monster_range:
        cr = random.choice(list(cr_dict.items()))[0]
        monster_range = encounters[party_level - 1][cr_dict[cr]]

    index = random.randint(0, len(monsters_cr) - 1)
    while monsters_cr[index] != cr:
        index = random.randint(0, len(monsters_cr) - 1)

    num = random.randint(monster_range[0], monster_range[len(monster_range) - 1])
    xp = num * xp_by_cr[cr]
    diff = difficulty(party_level, party_size, xp)

    print("you encounter " + str(num) + " " + monsters[index] + " for " + str(xp) + " XP and will be " + diff[0])
    return [0, num, monsters[index], xp, diff[0], cr]


def difficulty(level, size, encounter_xp):
    scaled_xp = encounter_xp/size
    xp_by_level = {
         '1': {'easy':   25, 'medium':   50, 'hard':   75, 'deadly':   100},
         '2': {'easy':   50, 'medium':  100, 'hard':  150, 'deadly':   200},
         '3': {'easy':   75, 'medium':  150, 'hard':  225, 'deadly':   400},
         '4': {'easy':  125, 'medium':  250, 'hard':  375, 'deadly':   500},
         '5': {'easy':  250, 'medium':  500, 'hard':  750, 'deadly':  1100},
         '6': {'easy':  300, 'medium':  600, 'hard':  900, 'deadly':  1400},
         '7': {'easy':  350, 'medium':  750, 'hard': 1100, 'deadly':  1700},
         '8': {'easy':  450, 'medium':  900, 'hard': 1400, 'deadly':  2100},
         '9': {'easy':  550, 'medium': 1100, 'hard': 1600, 'deadly':  2400},
         '10': {'easy':  600, 'medium': 1200, 'hard': 1900, 'deadly':  2800},
         '11': {'easy':  800, 'medium': 1600, 'hard': 2400, 'deadly':  3600},
         '12': {'easy': 1000, 'medium': 2000, 'hard': 3000, 'deadly':  4500},
         '13': {'easy': 1100, 'medium': 2200, 'hard': 3400, 'deadly':  5100},
         '14': {'easy': 1250, 'medium': 2500, 'hard': 3800, 'deadly':  5700},
         '15': {'easy': 1400, 'medium': 2800, 'hard': 4300, 'deadly':  6400},
         '16': {'easy': 1600, 'medium': 3200, 'hard': 4800, 'deadly':  7200},
         '17': {'easy': 2000, 'medium': 3900, 'hard': 5900, 'deadly':  8800},
         '18': {'easy': 2100, 'medium': 4200, 'hard': 6300, 'deadly':  9500},
         '19': {'easy': 2400, 'medium': 4900, 'hard': 7300, 'deadly': 10900},
         '20': {'easy': 2800, 'medium': 5700, 'hard': 8500, 'deadly': 12700},
         '21': {'easy': 3200, 'medium': 6400, 'hard': 9600, 'deadly': 14400},
    }
    xp_dict = xp_by_level[str(level)]
    if scaled_xp < xp_dict['medium']:
        return ['easy']
    elif scaled_xp < xp_dict['hard']:
        return ['medium']
    elif scaled_xp < xp_dict['deadly']:
        return ['hard']
    else:
        return ['deadly']


def getEvent(size, level, monster_list, cr_list):
    event = random.randint(0, 19)
    enc_chance = 6
    loot_chance = 6
    shop_chance = 4
    bor_chance = 2
    if event < enc_chance:
        event_key = randomEncounter(size, level, monster_list, cr_list)
    elif event < enc_chance + loot_chance:
        event_key = randomLoot(party_level)
    elif event < enc_chance + loot_chance + shop_chance:
        event_key = randomShop()
    elif event < enc_chance + loot_chance + shop_chance + bor_chance:
        event_key = boringEvent()
    else: #dungeon chance
        event_key = randomDungeon()

    return event_key


party_size = 4
party_level = 6
#party_level = int(input("enter avg party level: "))

monsters, monsters_cr = monsterParser('monsterlist')

shop_tab = 0
dung_tab = 0

event_list = []
event_dict = {0: 'encounter', 1: 'loot', 2: 'shop', 3: 'boring', 4: 'dungeon'}

for count in range(0, 20):
    print(str(count + 1) + ": ", end='')
    evnt = getEvent(party_size, party_level, monsters, monsters_cr)
    event_list.append(evnt)

roll = int(input("roll a die: "))
roll -= 1
if event_dict[event_list[roll][0]] == 'shop':
    webbrowser.open('https://rpgmarketgenerator.com/Town/create')
elif event_dict[event_list[roll][0]] == 'encounter':
    site = 'http://chisaipete.github.io/bestiary/creatures/'
    webbrowser.open(''.join([site, event_list[roll][2].replace(' ', '-').lower()]))
    loot = 'https://donjon.bin.sh/5e/random/#type=treasure;cr='+event_list[roll][5]+';loot_type=Individual%20Treasure'
    webbrowser.open(loot)
elif event_dict[event_list[roll][0]] == 'loot':
    webbrowser.open('https://donjon.bin.sh/5e/random/#type=magic_item;rarity=' + event_list[roll][1].replace(' ', '%20'))
    print('select number ' + str(event_list[roll][2]))
elif event_dict[event_list[roll][0]] == 'dungeon':
    webbrowser.open('https://donjon.bin.sh/5e/dungeon/')
else:  # boring
    pass






