import random
import webbrowser

"""This reads from a file (monsterlist) and returns two lists of monster names and monster's cr"""
def monsterParser(file):
    #open a file
    f = open(file, "r")
    #read everything into a string
    file_contents = f.read()
    #init variables
    name = []
    name_list = []
    cr = []
    cr_list = []
    #column keeps up with the column number
    column = 0
    prev_letter = ''

    #for every letter in the string
    for letter in file_contents:
        #if it is a tab symbol
        if letter == '\t':
            #if last letter was also a tab
            if prev_letter != '\t':
                #add to the counter
                column += 1
        #if there is a newline its a new monster
        elif letter == '\n':
            #reset variables and append to the lists
            column = 0
            name_list.append(''.join(name))
            cr_list.append(''.join(cr))
            name = []
            cr = []
        #if its the first column add to the name letter by letter
        elif column == 0:
            name.append(letter)
        #if its the 4th column sometimes this is alignment and other times it is cr
        elif column == 4:
            #if it is alignment
            if letter == 'L' or letter == 'N' or letter == 'C' or letter == 'U' or letter == 'A':
                #we are one column off
                column -= 1
            #if it is cr
            else:
                cr.append(letter)
        #anything else just ignore
        else:
            pass
        #keep up with the previous letter to stop double tabs from messing with col count
        prev_letter = letter
    #return our lists
    return name_list, cr_list

#generates a random shop and returns an event type enum, shop type, min rare, and max rare
def randomShop():
    #setup dicts
    rare_dict = {0: 'common', 1: 'uncommon', 2: 'rare', 3: 'very rare', 4: 'legendary'}
    shop_dict = {0: 'blacksmith', 1: 'wand maker', 2: 'enchanter', 3: 'alchemist'}
    #generate rarity limits
    min_rarity = random.randint(0,4)
    max_rarity = random.randint(0,4)
    #if min > max swap them
    if min_rarity > max_rarity:
        temp = min_rarity
        min_rarity = max_rarity
        max_rarity = temp
    #choose a type
    shop_type = random.randint(0,3)
    #fix articles
    if shop_dict[shop_type] == 'enchanter' or shop_dict[shop_type] == 'alchemist':
        article = 'an '
    else:
        article = 'a '
    #print output
    if min_rarity == max_rarity:
        print('you find ' + article + shop_dict[shop_type] + ' with ' + rare_dict[max_rarity] + ' items')
    else:
        print('you find ' + article + shop_dict[shop_type] + ' with ' + rare_dict[min_rarity] + ' to ' + rare_dict[
            max_rarity] + ' items')
    return [2, shop_dict[shop_type], rare_dict[min_rarity], rare_dict[max_rarity]]

#generates some random loot and returns event type enum, rarity, and which number to pick from the webpage
def randomLoot(level):
    #does some basic chance scaling
    common_chance = -abs(level-1)+16
    uncommon_chance = -abs(level-5)+16
    rare_chance = -abs(level-9)+16
    very_rare_chance = -abs(level-13)+16
    legendary_chance = -abs(level-17)+16
    total = common_chance + uncommon_chance + rare_chance + very_rare_chance + legendary_chance
    #setup rarity ranges
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
    #get a rarity
    roll = random.randint(1, 10)
    print(temp + ' loot')
    return [1, temp, roll]

#creates a boring event. returns event enum
def boringEvent():
    print("nothing exciting happens")
    return [3]

#creates a dungeon event. returns event enum
def randomDungeon():
    print("you find a hidden dungeon")
    return [4]

#hot garbage function that generates an encounter
#only supports party of 4 currently
#returns event enum, number of monsters, xp, difficulty, and cr
def randomEncounter(party_size, party_level, monsters, monsters_cr):
    #xp by cr dict
    xp_by_cr = {
        '0': 10, '1/8': 25, '1/4': 50, '1/2': 100,
        '1': 200, '2': 450, '3': 700, '4': 1100,
        '5': 1800, '6': 2300, '7': 2900, '8': 3900,
        '9': 5000, '10': 5900, '11': 7200, '12': 8400,
        '13': 10000, '14': 11500, '15': 13000, '16': 15000,
        '17': 18000, '18': 20000, '19': 22000, '20': 25000,
    }

    #gets encounter size range if you have a party size of 4
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

    #convert cr to index
    cr_dict = {'0': 0, '1/8': 1, '1/4': 2, '1/2': 3}
    #auto generate the rest
    temp = {str(x): x + 3 for x in range(1, 20)}
    cr_dict.update(temp)

    #choose a cr
    cr = random.choice(list(cr_dict.items()))[0]
    #get the range of monsters
    monster_range = encounters[party_level - 1][cr_dict[cr]]
    #if no range available
    while not monster_range:
        #choose again
        cr = random.choice(list(cr_dict.items()))[0]
        monster_range = encounters[party_level - 1][cr_dict[cr]]

    #get a random monster type
    index = random.randint(0, len(monsters_cr) - 1)
    #if the cr is not right choose again
    while monsters_cr[index] != cr:
        index = random.randint(0, len(monsters_cr) - 1)

    #choose a number in the range of number of monsters
    num = random.randint(monster_range[0], monster_range[len(monster_range) - 1])
    #calc xp
    xp = num * xp_by_cr[cr]
    #get difficulty
    diff = difficulty(party_level, party_size, xp)

    #print output
    print("you encounter " + str(num) + " " + monsters[index] + " for " + str(xp) + " XP and will be " + diff[0])
    return [0, num, monsters[index], xp, diff[0], cr]

#gets difficulty basec on avg level, xp of encounter, and party size
def difficulty(level, size, encounter_xp):
    #get xp per person
    scaled_xp = encounter_xp/size
    #make a dict
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
    #read the dict for your level
    xp_dict = xp_by_level[str(level)]
    #read the dict for diff
    if scaled_xp < xp_dict['medium']:
        return ['easy']
    elif scaled_xp < xp_dict['hard']:
        return ['medium']
    elif scaled_xp < xp_dict['deadly']:
        return ['hard']
    else:
        return ['deadly']

#get a random event and return the event tupe
def getEvent(size, level, monster_list, cr_list):
    #setup event frequencies
    enc_chance = 6
    loot_chance = 6
    shop_chance = 4
    bor_chance = 2
    #choose an event
    event = random.randint(0, (enc_chance+loot_chance+shop_chance+bor_chance+1))
    #choose an event and call an appropriate function
    if event < enc_chance:
        event_key = randomEncounter(size, level, monster_list, cr_list)
    elif event < enc_chance + loot_chance:
        event_key = randomLoot(level)
    elif event < enc_chance + loot_chance + shop_chance:
        event_key = randomShop()
    elif event < enc_chance + loot_chance + shop_chance + bor_chance:
        event_key = boringEvent()
    else: #dungeon chance
        event_key = randomDungeon()
    #return the event enum
    return event_key

#main function
def main():
    #get party info
    party_size = 4
    party_level = int(input("enter avg party level: "))

    #get monsters
    monsters, monsters_cr = monsterParser('monsterlist')

    #setup event dict
    event_list = []
    event_dict = {0: 'encounter', 1: 'loot', 2: 'shop', 3: 'boring', 4: 'dungeon'}

    #create 20 events
    for count in range(0, 20):
        print(str(count + 1) + ": ", end='')
        evnt = getEvent(party_size, party_level, monsters, monsters_cr)
        event_list.append(evnt)

    #ask for a die roll
    roll = int(input("roll a die: "))
    #convert to index
    roll -= 1
    #open appropriate webpage for choice. Currently user fills out most of the info based on output
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

if __name__ == "__main__":
    main()




