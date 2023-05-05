import csv
import random
import time
import sys
import os
import pandas as pd
import math
import vlc

PokemonList = 'C:/code/git/PythonProjects/Projects/RandomPokemonFight/Pokemon.csv'
Pokemon_dct = {}
PokemonMovesList = 'C:/code/git/PythonProjects/Projects/RandomPokemonFight/PokemonMoves.csv'
PokemonMoves_dct = {}
Intro_music = vlc.MediaPlayer("C:/code/git/PythonProjects/Projects/RandomPokemonFight/Intro.wav")
Battle_music = vlc.MediaPlayer("C:/code/git/PythonProjects/Projects/RandomPokemonFight/Battle.wav")
Victory_music = vlc.MediaPlayer("C:/code/git/PythonProjects/Projects/RandomPokemonFight/Victory.wav")
P1Moves = {}
P2Moves = {}
P1Username = ""
P2Username = ""
col=0
P1Pokemon = ""
P1Type = ""
P1Atk = 0
P1Def = 0
P1SpAtk = 0
P1SpDef = 0
P1Spd = 0
P1Hp = 0
P2Pokemon = ""
P2Type = ""
P2Atk = 0
P2Def = 0
P2SpAtk = 0
P2SpDef = 0
P2Spd = 0
P2Hp = 0
P1M1Name = ""
P1M1Type = ""
P1M1Dmg = 0
P1M1DmgType = ""
P1M1Acc = 0
P1M2Name = ""
P1M2Type = ""
P1M2Dmg = 0
P1M2DmgType = ""
P1M2Acc = 0
P1M3Name = ""
P1M3Type = ""
P1M3Dmg = 0
P1M3DmgType = ""
P1M3Acc = 0
P1M4Name = ""
P1M4Type = ""
P1M4Dmg = 0
P1M4DmgType = ""
P1M4Acc = 0
P2M1Name = ""
P2M1Type = ""
P2M1Dmg = 0
P2M1DmgType = ""
P2M1Acc = 0
P2M2Name = ""
P2M2Type = ""
P2M2Dmg = 0
P2M2DmgType = ""
P2M2Acc = 0
P2M3Name = ""
P2M3Type = ""
P2M3Dmg = 0
P2M3DmgType = ""
P2M3Acc = 0
P2M4Name = ""
P2M4Type = ""
P2M4Dmg = 0
P2M4DmgType = ""
P2M4Acc = 0
random_move_P1M1 = ""
random_move_P1M2 = ""
random_move_P2M1 = ""
random_move_P2M2 = ""
P1Health_Visual = ""
P2Health_Visual = ""
P1Healthbars = ""
P2Healthbars = ""
mult = int(1)
random_pkmn1 = ""
random_pkmn2 = ""
random_pkmn3 = ""
random_pkmn4 = ""
random_pkmn5 = ""
random_pkmn6 = ""
random_moveP1M3 = ""
random_moveP1M4 = ""
random_moveP2M3 = ""
random_moveP2M4 = ""
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, type1, Hp, Atk, Def, SpAtk, SpDef, Spd):
        self.name = name
        self.type1 = type1
        self.Atk = Atk
        self.Def = Def
        self.SpAtk = SpAtk
        self.SpDef = SpDef
        self.Spd = Spd
        self.Hp = Hp

    def pokechoice(self):
        name = self.name
        Pokechoice = (f"{name}")
        return Pokechoice

    def pokeinfo1(self):
        global P1Pokemon
        global P1Type
        global P1Atk
        global P1Def
        global P1SpAtk
        global P1SpDef
        global P1Spd
        global P1Hp
        name1 = self.name
        pkmntype1 = self.type1
        Atk1 = self.Atk
        Def1 = self.Def
        SpAtk1 = self.SpAtk
        SpDef1 = self.SpDef
        Spd1 = self.Spd
        Hp1 = self.Hp

        P1Pokemon = (f"{name1}")
        P1Type = (f"{pkmntype1}")
        P1Atk = int(Atk1)
        P1Def = int(Def1)
        P1SpAtk = int(SpAtk1)
        P1SpDef = int(SpDef1)
        P1Spd = int(Spd1)
        P1Hp = int(Hp1)

    def pokeinfo2(self):
        global P2Pokemon
        global P2Type
        global P2Atk
        global P2Def
        global P2SpAtk
        global P2SpDef
        global P2Spd
        global P2Hp
        name2 = self.name
        pkmntype2 = self.type1
        Atk2 = self.Atk
        Def2 = self.Def
        SpAtk2 = self.SpAtk
        SpDef2 = self.SpDef
        Spd2 = self.Spd
        Hp2 = self.Hp

        P2Pokemon = (f"{name2}")
        P2Type = (f"{pkmntype2}")
        P2Atk = int(Atk2)
        P2Def = int(Def2)
        P2SpAtk = int(SpAtk2)
        P2SpDef = int(SpDef2)
        P2Spd = int(Spd2)
        P2Hp = int(Hp2)

class Moves:
    def __init__(self, name, type, damage_type, damage, accuracy):
        self.name = name
        self.type = type
        self.damage = damage
        self.damage_type = damage_type
        self.accuracy = accuracy

    def moveinfoP1M1(self):
        global P1M1Name
        global P1M1Type
        global P1M1Dmg
        global P1M1DmgType
        global P1M1Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P1M1Name = name
        P1M1Type = type
        P1M1Dmg = dmg
        P1M1DmgType = dmg_type
        P1M1Acc = accuracy
    def moveinfoP1M2(self):
        global P1M2Name
        global P1M2Type
        global P1M2Dmg
        global P1M2DmgType
        global P1M2Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P1M2Name = name
        P1M2Type = type
        P1M2Dmg = dmg
        P1M2DmgType = dmg_type
        P1M2Acc = accuracy
    def moveinfoP1M3(self):
        global P1M3Name
        global P1M3Type
        global P1M3Dmg
        global P1M3DmgType
        global P1M3Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P1M3Name = name
        P1M3Type = type
        P1M3Dmg = dmg
        P1M3DmgType = dmg_type
        P1M3Acc = accuracy
    def moveinfoP1M4(self):
        global P1M4Name
        global P1M4Type
        global P1M4Dmg
        global P1M4DmgType
        global P1M4Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P1M4Name = name
        P1M4Type = type
        P1M4Dmg = dmg
        P1M4DmgType = dmg_type
        P1M4Acc = accuracy
    def moveinfoP2M1(self):
        global P2M1Name
        global P2M1Type
        global P2M1Dmg
        global P2M1DmgType
        global P2M1Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P2M1Name = name
        P2M1Type = type
        P2M1Dmg = dmg
        P2M1DmgType = dmg_type
        P2M1Acc = accuracy
    def moveinfoP2M2(self):
        global P2M2Name
        global P2M2Type
        global P2M2Dmg
        global P2M2DmgType
        global P2M2Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P2M2Name = name
        P2M2Type = type
        P2M2Dmg = dmg
        P2M2DmgType = dmg_type
        P2M2Acc = accuracy
    def moveinfoP2M3(self):
        global P2M3Name
        global P2M3Type
        global P2M3Dmg
        global P2M3DmgType
        global P2M3Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P2M3Name = name
        P2M3Type = type
        P2M3Dmg = dmg
        P2M3DmgType = dmg_type
        P2M3Acc = accuracy
    def moveinfoP2M4(self):
        global P2M4Name
        global P2M4Type
        global P2M4Dmg
        global P2M4DmgType
        global P2M4Acc
        name = self.name
        type = self.type
        dmg = int(self.damage)
        dmg_type = self.damage_type
        accuracy = float(self.accuracy)
        P2M4Name = name
        P2M4Type = type
        P2M4Dmg = dmg
        P2M4DmgType = dmg_type
        P2M4Acc = accuracy

with open(f'{PokemonList}', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        Pokemon_dct[row[0]] = Pokemon(row[0], row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]))

with open(f'{PokemonMovesList}', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        PokemonMoves_dct[row[0]] = Moves(row[0], row[1], row[2], int(row[3]), float(row[4]))

def Pokemon_Randomizer():
    global random_pkmn1
    global random_pkmn2
    global random_pkmn3
    global random_pkmn4
    global random_pkmn5
    global random_pkmn6
    with open(f'{PokemonList}', 'r') as f:
        reader = csv.reader(f)
        data = [row[col] for row in reader]
        random_pkmn1 = random.choice(data)
        random_pkmn2 = random.choice(data)
        random_pkmn3 = random.choice(data)
        random_pkmn4 = random.choice(data)
        random_pkmn5 = random.choice(data)
        random_pkmn6 = random.choice(data)

def pkmn_choice1():
    Pokemon1 = Pokemon_dct[f'{random_pkmn1}'].pokechoice()
    Pokemon2 = Pokemon_dct[f'{random_pkmn2}'].pokechoice()
    Pokemon3 = Pokemon_dct[f'{random_pkmn3}'].pokechoice()
    choices1 = [f'{Pokemon1}', f'{Pokemon2}', f'{Pokemon3}']
    print("Choose one of these Pokemon to fight with.")
    userinput1 = ""
    while userinput1 not in choices1:
        print(f"Options: {Pokemon1}, {Pokemon2}, or {Pokemon3}.")
        userinput1 = input("")
        if userinput1 in [f"{Pokemon1}", f"{Pokemon2}", f"{Pokemon3}"]:
            delay_print(f'You have chosen {userinput1} to be your partner.')
            time.sleep(1)
            Pokemon_dct[f'{userinput1}'].pokeinfo1()
        else:
            print("That was not a valid selection. Please try again")

def pkmn_choice2():
    Pokemon4 = Pokemon_dct[f'{random_pkmn4}'].pokechoice()
    Pokemon5 = Pokemon_dct[f'{random_pkmn5}'].pokechoice()
    Pokemon6 = Pokemon_dct[f'{random_pkmn6}'].pokechoice()
    choices2 = [f"{Pokemon4}", f"{Pokemon5}", f"{Pokemon6}"]
    print("Choose one of these Pokemon to Fight with.")
    userinput2 = ""
    while userinput2 not in choices2:
        print(f"Options: {Pokemon4}, {Pokemon5}, or {Pokemon6}.")
        userinput2 = input()
        if userinput2 in [f"{Pokemon4}", f"{Pokemon5}", f"{Pokemon6}"]:
            delay_print(f'You have chosen {userinput2} to be your partner.')
            time.sleep(1)
            Pokemon_dct[f'{userinput2}'].pokeinfo2()
        else:
            print("That was not a valid selection. Please try again.")

def Pokemon_Selection():
    global P1Pokemon
    global P2Pokemon
    global P1Username
    global P2Username
    global random_pkmn1
    global random_pkmn2
    global random_pkmn3
    global random_pkmn4
    global random_pkmn5
    global random_pkmn6
    Pokemon_Randomizer()
    print(f"\nPlease pass the computer to {P1Username}")
    input(f"\n{P1Username}, Press Enter to Continue: ")
    time.sleep(1)
    pkmn_choice1()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nPlease pass the computer to {P2Username}")
    input(f"\n{P2Username}, Press Enter to Continue: ")
    time.sleep(1)
    pkmn_choice2()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    delay_print(f"\n{P1Username} has chosen {P1Pokemon}.")
    delay_print(f"\n{P2Username} has chosen {P2Pokemon}.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def full_random_move():
    global random_moveP1M3
    global random_moveP1M4
    global random_moveP2M3
    global random_moveP2M4
    with open(f'{PokemonMovesList}', 'r') as f:
        reader = csv.reader(f)
        data = [row[col] for row in reader]
        random_moveP1M3 = random.choice(data)
        random_moveP1M4 = random.choice(data)
        random_moveP2M3 = random.choice(data)
        random_moveP2M4 = random.choice(data)

def target_random_move_P1M1():
    global P1Type
    global random_move_P1M1
    df = pd.read_csv(f"{PokemonMovesList}", header = None)
    df = df.loc[df[1] == f'{P1Type}']
    df = df.loc[:,0]
    df = df.sample()
    random_move_P1M1 = df.values[0]

def target_random_move_P1M2():
    global P1Type
    global random_move_P1M2
    df = pd.read_csv(f"{PokemonMovesList}", header = None)
    df = df.loc[df[1] == f'{P1Type}']
    df = df.loc[:,0]
    df = df.sample()
    random_move_P1M2 = df.values[0]

def target_random_move_P2M1():
    global P2Type
    global random_move_P2M1
    df = pd.read_csv(f"{PokemonMovesList}", header = None)
    df = df.loc[df[1] == f'{P2Type}']
    df = df.loc[:,0]
    df = df.sample()
    random_move_P2M1 = df.values[0]

def target_random_move_P2M2():
    global P2Type
    global random_move_P2M2
    df = pd.read_csv(f"{PokemonMovesList}", header = None)
    df = df.loc[df[1] == f'{P2Type}']
    df = df.loc[:,0]
    df = df.sample()
    random_move_P2M2 = df.values[0]

def Move_info_Generator():
    global random_move_P1M1
    global random_move_P1M2
    global random_move_P2M1
    global random_move_P2M2
    PokemonMoves_dct[f'{random_move_P1M1}'].moveinfoP1M1()
    PokemonMoves_dct[f'{random_move_P1M2}'].moveinfoP1M2()
    PokemonMoves_dct[f'{random_moveP1M3}'].moveinfoP1M3()
    PokemonMoves_dct[f'{random_moveP1M4}'].moveinfoP1M4()
    PokemonMoves_dct[f'{random_move_P2M1}'].moveinfoP2M1()
    PokemonMoves_dct[f'{random_move_P2M2}'].moveinfoP2M2()
    PokemonMoves_dct[f'{random_moveP2M3}'].moveinfoP2M3()
    PokemonMoves_dct[f'{random_moveP2M4}'].moveinfoP2M4()

def Move_Generator():
    global P1Moves
    global P2Moves
    P1Moves = {f'{P1M1Name}': [f'{P1M1Type}'], f'{P1M2Name}': [f'{P1M2Type}'], f'{P1M3Name}': [f'{P1M3Type}'], f'{P1M4Name}': [f'{P1M4Type}'],}
    P1Moves[f'{P1M1Name}'] += [int(f'{P1M1Dmg}'), f'{P1M1DmgType}', float(f'{P1M1Acc}')]
    P1Moves[f'{P1M2Name}'] += [int(f'{P1M2Dmg}'), f'{P1M2DmgType}', float(f'{P1M2Acc}')]
    P1Moves[f'{P1M3Name}'] += [int(f'{P1M3Dmg}'), f'{P1M3DmgType}', float(f'{P1M3Acc}')]
    P1Moves[f'{P1M4Name}'] += [int(f'{P1M4Dmg}'), f'{P1M4DmgType}', float(f'{P1M4Acc}')]
    P2Moves = {f'{P2M1Name}': [f'{P2M1Type}'], f'{P2M2Name}': [f'{P2M2Type}'], f'{P2M3Name}': [f'{P2M3Type}'], f'{P2M4Name}': [f'{P2M4Type}'], }
    P2Moves[f'{P2M1Name}'] += [int(f'{P2M1Dmg}'), f'{P2M1DmgType}', float(f'{P2M1Acc}')]
    P2Moves[f'{P2M2Name}'] += [int(f'{P2M2Dmg}'), f'{P2M2DmgType}', float(f'{P2M2Acc}')]
    P2Moves[f'{P2M3Name}'] += [int(f'{P2M3Dmg}'), f'{P2M3DmgType}', float(f'{P2M3Acc}')]
    P2Moves[f'{P2M4Name}'] += [int(f'{P2M4Dmg}'), f'{P2M4DmgType}', float(f'{P2M4Acc}')]

def Intro():
    global P1Username
    global P2Username
    Intro_music.play()
    delay_print("Hello!\nWelcome to Pokemon Battle!")
    delay_print("\nFirst off, what are your names?")
    time.sleep(1)
    delay_print("\nPlayer one, please enter your name: ")
    P1Username = input()
    delay_print(f"\nIt\'s nice to meet you {P1Username} and best of luck in your Pokemon Battle!")
    time.sleep(1)
    delay_print("\nPlayer two, please enter your name: ")
    P2Username = input()
    delay_print(f"\nIt\'s nice to meet you {P2Username} and best of luck in your Pokemon Battle!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("\nEach of you will be given 3 Pokemon to choose from.")
    delay_print("\nYou then will choose one of those 3 to participate in a Pokemon Battle!")
    delay_print("\nYou will now each select your Pokemon.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def create_healthbar():
    global P1Hp
    global P2Hp
    global P1Health_Visual
    global P2Health_Visual
    global P1Healthbars
    global P2Healthbars
    P1Health_Visual = ('='*int(int(f'{P1Hp}')/5))
    P2Health_Visual = ('='*int(int(f'{P2Hp}')/5))
    P1Healthbars = int(int(f'{P1Hp}')/5)
    P2Healthbars = int(int(f'{P2Hp}')/5)

def Battle_Start():
    global P1Spd
    Battle_music.play()
    if int(f'{P1Spd}') > int(f'{P2Spd}'):
        delay_print(f'\n{P1Username} sends out {P1Pokemon}.')
        delay_print(f'\n{P2Username} sends out {P2Pokemon}.')
        os.system('cls' if os.name == 'nt' else 'clear')
        fight_P1_Fast()
        Battle_End()

    if int(f'{P2Spd}') > int(f'{P1Spd}'):
        delay_print(f'\n{P2Username} sends out {P2Pokemon}')
        delay_print(f'\n{P1Username} sends out {P1Pokemon}')
        os.system('cls' if os.name == 'nt' else 'clear')
        fight_P2_Fast()
        Battle_End()

    else:
        spdmod = random.randint(-1, 1)
        P1Spd = (int(f'{P1Spd}') + int(f'{spdmod}'))
        Battle_Start()

def fight_P1_Fast():
    global mult
    global P1Healthbars
    global P1Health_Visual
    global P2Healthbars
    global P2Health_Visual
    while (P1Healthbars > 0) and (P2Healthbars > 0):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n{P1Health_Visual}')
        print(f'\n{P1Pokemon}')
        print(f'\n{P2Health_Visual}')
        print(f'\n{P2Pokemon}')
        time.sleep(3)
        P1_Attack()
        if P2Healthbars > 0:
            P2_Attack()
        else:
            break

def fight_P2_Fast():
    global mult
    global P1Healthbars
    global P1Health_Visual
    global P2Healthbars
    global P2Health_Visual
    while (P1Healthbars > 0) and (P2Healthbars > 0):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n{P2Health_Visual}')
        print(f'\n{P2Pokemon}')
        print(f'\n{P1Health_Visual}')
        print(f'\n{P1Pokemon}')
        time.sleep(3)
        P2_Attack()
        if P1Healthbars > 0:
            P1_Attack()
        else:
            break
def type_effectiveness(move_type, pokemon_type):
    global mult
    if move_type == 'Normal':
        if pokemon_type == 'Ghost':
            mult = int(0)
        elif pokemon_type in ['Steel', 'Rock',]:
            mult = float(0.5)
        else:
            mult = int(1)
    elif move_type == 'Poison':
        if pokemon_type == 'Steel':
            mult = int(0)
        elif pokemon_type in ['Poison', 'Ground']:
            mult = float(0.5)
        elif pokemon_type in ['Grass', 'Fairy']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Psychic':
        if pokemon_type == 'Dark':
            mult = int(0)
        elif pokemon_type in ['Psychic', 'Steel']:
            mult = float(0.5)
        elif pokemon_type in ['Poison', 'Fighting']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Rock':
        if pokemon_type in ['Ground', 'Steel', 'Fighting']:
            mult = float(0.5)
        elif pokemon_type in ['Bug', 'Flying', 'Ice', 'Fire']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Steel':
        if pokemon_type in ['Steel', 'Water', 'Fire']:
            mult = float(0.5)
        elif pokemon_type in ['Fairy', 'Rock', 'Ice']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Water':
        if pokemon_type in ['Water', 'Grass' ,'Dragon']:
            mult = float(0.5)
        elif pokemon_type in ['Rock', 'Ground', 'Fire']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Fire':
        if pokemon_type in ['Fire', 'Rock', 'Water', 'Dragon']:
            mult = float(0.5)
        elif pokemon_type in ['Grass', 'Bug', 'Ice']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Flying':
        if pokemon_type in ['Steel', 'Rock', 'Electric']:
            mult = float(0.5)
        elif pokemon_type in ['Grass', 'Bug', 'Fighting']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Ghost':
        if pokemon_type == 'Normal':
            mult = int(0)
        elif pokemon_type in ['Dark']:
            mult = float(0.5)
        elif pokemon_type in ['Psychic', 'Ghost']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Grass':
        if pokemon_type in ['Grass', 'Poison', 'Bug', 'Steel', 'Dragon']:
            mult = float(0.5)
        elif pokemon_type in ['Water', 'Rock', 'Ground']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Ground':
        if pokemon_type == 'Flying':
            mult = int(0)
        elif pokemon_type in ['Grass', 'Bug']:
            mult = float(0.5)
        elif pokemon_type in ['Rock', 'Steel', 'Poison', 'Electric']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Ice':
        if pokemon_type in ['Steel', 'Fire', 'Water']:
            mult = float(0.5)
        elif pokemon_type in ['Grass', 'Flying', 'Ground', 'Dragon']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Bug':
        if pokemon_type in ['Steel', 'Fire', 'Fighting', 'Flying', 'Poison', 'Fairy']:
            mult = float(0.5)
        elif pokemon_type in ['Psychic', 'Ghost', 'Grass', 'Dark']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Dark':
        if pokemon_type in ['Fighting', 'Dark', 'Fairy']:
            mult = float(0.5)
        elif pokemon_type in ['Psychic', 'Ghost']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Dragon':
        if pokemon_type == 'Fairy':
            mult = int(0)
        elif pokemon_type in ['Steel']:
            mult = float(0.5)
        elif pokemon_type == 'Dragon':
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Electric':
        if pokemon_type == 'Ground':
            mult = int(0)
        elif pokemon_type in ['Grass']:
            mult = float(0.5)
        elif pokemon_type in ['Water', 'Flying']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Fairy':
        if pokemon_type in ['Steel', 'Fire', 'Poison']:
            mult = float(0.5)
        elif pokemon_type in ['Dark', 'Fighting']:
            mult = int(2)
        else:
            mult = int(1)
    elif move_type == 'Fighting':
        if pokemon_type == 'Ghost':
            mult = int(0)
        elif pokemon_type in ['Flying', 'Poison', 'Bug']:
            mult = float(0.5)
        elif pokemon_type in ['Steel', 'Rock', 'Normal', 'Ice']:
            mult = int(2)
        else:
            mult = int(1)



def Battle_End():
    Battle_music.stop()
    Victory_music.play()
    if P1Healthbars <= 0:
        delay_print(f'\nOh no! {P1Pokemon} has fainted!')
        delay_print(f'\n{P2Username} wins!')
        payout = random.randint(0,5000)
        delay_print(f'\n{P1Username} paid ${payout} to {P2Username}')
        delay_print(f'\nWould you like to play again? (y/n)')
        again = input("\n")
        if again == 'y':
            Victory_music.stop()
            Intro_music.play()
            replay()
        else:
            delay_print(f"\nGoodbye {P1Username} and {P2Username}. Thank you for playing Pokemon Battle!")
            quit()
    else:
        delay_print(f'\nOh no! {P2Pokemon} has fainted!')
        delay_print(f'\n{P1Username} wins!')
        payout = random.randint(0, 5000)
        delay_print(f'\n{P2Username} paid ${payout} to {P1Username}')
        delay_print(f'\nWould you like to play again? (y/n)')
        again = input("\n")
        if again == 'y':
            Victory_music.stop()
            Intro_music.play()
            replay()
        else:
            delay_print(f"\nGoodbye {P1Username} and {P2Username}. Thank you for playing Pokemon Battle!")
            quit()


def P1_Attack():
    global mult
    global P1Healthbars
    global P1Health_Visual
    global P2Healthbars
    global P2Health_Visual
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print(f'{P1Username}, which move should {P1Pokemon} use?')
    moves = [f"{P1M1Name}", f"{P1M2Name}", f"{P1M3Name}", f"{P1M4Name}"]
    selection = ""
    while selection not in moves:
        print(f"\nOptions: \n{P1M1Name}\n{P1M2Name}\n{P1M3Name}\n{P1M4Name}")
        selection = input()
        if selection in [f"{P1M1Name}", f"{P1M2Name}", f"{P1M3Name}", f"{P1M4Name}"]:
            acc_check = random.random()
            delay_print(f'\n{P1Pokemon} used {selection}!')
            if acc_check <= (P1Moves[f'{selection}'][3]):
                if (P1Moves[f'{selection}'][2]) == 'Physical':
                    notypephysdmg = int((((P1Moves[f'{selection}'][1]) * ((int(f'{P1Atk}')) / (int(P2Def)))) / 30) + 1)
                    type_effectiveness((P1Moves[f'{selection}'][0]), P2Type)
                    physdmg = ((int(f'{notypephysdmg}')) * (float(f'{mult}')))
                    if mult == 2:
                        delay_print('\nThe attack will be super effective!!!')
                    elif mult == 0.5:
                        delay_print('\nThe attack will be not very effective...')
                    elif mult == 0:
                        delay_print('\nThe attack will have no effect')
                    else:
                        delay_print('\nThe attack will be effective!')
                    if P1Type == (P1Moves[f'{selection}'][0]):
                        stat = float(float(f'{physdmg}') * 1.5)
                        stabphysdmg = math.ceil(float(f'{stat}'))
                        P2Healthbars = int(int(f'{P2Healthbars}') - int(f'{stabphysdmg}'))
                        P2Health_Visual = ('=' * int(int(f'{P2Healthbars}')))
                        delay_print(f'\n{selection} hit! {P2Pokemon} took {stabphysdmg} damage!')
                        time.sleep(2)
                    else:
                        physdmg = math.ceil(float(f'{physdmg}'))
                        P2Healthbars = int(int(f'{P2Healthbars}') - int(f'{physdmg}'))
                        P2Health_Visual = ('=' * int(int(f'{P2Healthbars}')))
                        delay_print(f'\n{selection} hit! {P2Pokemon} took {physdmg} damage!')
                        time.sleep(2)
                else:
                    notypespecdmg = int((((P1Moves[f'{selection}'][1]) * ((int(f'{P1SpAtk}')) / (int(P2SpDef)))) / 30) + 1)
                    type_effectiveness((P1Moves[f'{selection}'][0]), P2Type)
                    specdmg = ((int(f'{notypespecdmg}')) * (float(f'{mult}')))
                    if mult == 2:
                        delay_print('\nThe attack will be super effective!!!')
                    elif mult == 0.5:
                        delay_print('\nThe attack will be not very effective...')
                    elif mult == 0:
                        delay_print('\nThe attack will have no effect')
                    else:
                        delay_print('\nThe attack will be effective!')
                    if P1Type == (P1Moves[f'{selection}'][0]):
                        stat = float(float(f'{specdmg}') * 1.5)
                        stabspecdmg = math.ceil(float(f'{stat}'))
                        P2Healthbars = int(int(f'{P2Healthbars}') - int(f'{stabspecdmg}'))
                        P2Health_Visual = ('=' * int(int(f'{P2Healthbars}')))
                        delay_print(f'\n{selection} hit! {P2Pokemon} took {stabspecdmg} damage!')
                        time.sleep(2)
                    else:
                        specdmg = math.ceil(float(f'{specdmg}'))
                        P2Healthbars = int(int(f'{P2Healthbars}') - int(f'{specdmg}'))
                        P2Health_Visual = ('=' * int(int(f'{P2Healthbars}')))
                        delay_print(f'\n{selection} hit! {P2Pokemon} took {specdmg} damage!')
                        time.sleep(2)
            else:
                delay_print(f"\nOh no! {P1Pokemon} missed!")
                time.sleep(2)

        else:
            print("\nPlease choose a valid attack.")

def P2_Attack():
    global mult
    global P1Healthbars
    global P1Health_Visual
    global P2Healthbars
    global P2Health_Visual
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print(f'{P2Username}, which move should {P2Pokemon} use?')
    moves = [f"{P2M1Name}", f"{P2M2Name}", f"{P2M3Name}", f"{P2M4Name}"]
    selection = ""
    while selection not in moves:
        print(f"\nOptions: \n{P2M1Name}\n{P2M2Name}\n{P2M3Name}\n{P2M4Name}")
        selection = input()
        if selection in [f"{P2M1Name}", f"{P2M2Name}", f"{P2M3Name}", f"{P2M4Name}"]:
            acc_check = random.random()
            delay_print(f'\n{P2Pokemon} used {selection}!')
            if acc_check <= (P2Moves[f'{selection}'][3]):
                if (P2Moves[f'{selection}'][2]) == 'Physical':
                    notypephysdmg = int((((P2Moves[f'{selection}'][1]) * ((int(f'{P2Atk}')) / (int(P1Def)))) / 30) + 1)
                    type_effectiveness((P2Moves[f'{selection}'][0]), P1Type)
                    physdmg = ((int(f'{notypephysdmg}')) * (float(f'{mult}')))
                    if mult == 2:
                        delay_print('\nThe attack will be super effective!!!')
                    elif mult == 0.5:
                        delay_print('\nThe attack will be not very effective...')
                    elif mult == 0:
                        delay_print('\nThe attack will have no effect')
                    else:
                        delay_print('\nThe attack will be effective!')
                    if P2Type == (P2Moves[f'{selection}'][0]):
                        stat = float(float(f'{physdmg}') * 1.5)
                        stabphysdmg = math.ceil(float(f'{stat}'))
                        P1Healthbars = int(int(f'{P1Healthbars}') - int(f'{stabphysdmg}'))
                        P1Health_Visual = ('=' * int(int(f'{P1Healthbars}')))
                        delay_print(f'\n{selection} hit! {P1Pokemon} took {stabphysdmg} damage!')
                        time.sleep(2)
                    else:
                        physdmg = math.ceil(float(f'{physdmg}'))
                        P1Healthbars = int(int(f'{P1Healthbars}') - int(f'{physdmg}'))
                        P1Health_Visual = ('=' * int(int(f'{P1Healthbars}')))
                        delay_print(f'\n{selection} hit! {P1Pokemon} took {physdmg} damage!')
                        time.sleep(2)
                else:
                    notypespecdmg = int((((P2Moves[f'{selection}'][1]) * ((int(f'{P2SpAtk}')) / (int(P1SpDef)))) / 30) + 1)
                    type_effectiveness((P2Moves[f'{selection}'][0]), P1Type)
                    specdmg = ((int(f'{notypespecdmg}')) * (float(f'{mult}')))
                    if mult == 2:
                        delay_print('\nThe attack will be super effective!!!')
                    elif mult == 0.5:
                        delay_print('\nThe attack will be not very effective...')
                    elif mult == 0:
                        delay_print('\nThe attack will have no effect')
                    else:
                        delay_print('\nThe attack will be effective!')
                    if P2Type == (P2Moves[f'{selection}'][0]):
                        stat = float(float(f'{specdmg}') * 1.5)
                        stabspecdmg = math.ceil(float(f'{stat}'))
                        P1Healthbars = int(int(f'{P1Healthbars}') - int(f'{stabspecdmg}'))
                        P1Health_Visual = ('=' * int(int(f'{P1Healthbars}')))
                        delay_print(f'\n{selection} hit! {P1Pokemon} took {stabspecdmg} damage!')
                        time.sleep(2)
                    else:
                        specdmg = math.ceil(float(f'{specdmg}'))
                        P1Healthbars = int(int(f'{P1Healthbars}') - int(f'{specdmg}'))
                        P1Health_Visual = ('=' * int(int(f'{P1Healthbars}')))
                        delay_print(f'\n{selection} hit! {P1Pokemon} took {specdmg} damage!')
                        time.sleep(2)
            else:
                delay_print(f"\nOh no! {P2Pokemon} missed!")
                time.sleep(2)

        else:
            print("\nPlease choose a valid attack.")

def replay():
    os.system('cls' if os.name == 'nt' else 'clear')
    Pokemon_Selection()
    full_random_move()
    target_random_move_P1M1()
    target_random_move_P1M2()
    target_random_move_P2M1()
    target_random_move_P2M2()
    Move_info_Generator()
    Move_Generator()
    create_healthbar()
    Intro_music.stop()
    Battle_Start()

Intro()
replay()
