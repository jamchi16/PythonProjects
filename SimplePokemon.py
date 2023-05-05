import time
import numpy as np
import sys


# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack  = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20

    def fight(self, Pokemon2):
        print("POKEMON BATTLE")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")

        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))
        print("\nVS")

        time.sleep(2)

        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                if Pokemon2.types == k:
                    string_1_attack = 'It\'s not very effective...'
                    string_2_attack = 'It\'s not very effective...'
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = 'It\'s not very effective...'
                    string_2_attack = 'It\'s super effective!'
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_2_attack = 'It\'s not very effective...'
                    string_1_attack = 'It\'s super effective!'
        while (self.bars > 0) and (Pokemon2.bars > 0):
            print(f"{self.name}\t\tHEALTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{self.name} used {self.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHEALTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{Pokemon2.name} used {Pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            self.bars -= Pokemon2.attack
            self.health = ""

            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}")
            print(f"{self.name}\t\tHEALTH\t{self.health}\n")
            time.sleep(0.5)

            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break
        money = np.random.choice(5000)
        delay_print(f" Opponent paid you ${money}")












if __name__ == '__main__':
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro pump', 'Surf'], {'ATTACK': 8, 'DEFENSE': 10})

Charizard.fight(Blastoise)