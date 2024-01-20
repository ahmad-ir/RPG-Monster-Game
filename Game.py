import random
from Character import *
from Monster import *

# Assuming Character and Monster classes are defined in their respective files
# and imported here from Character import Character from Monster import Monster

class Game:

    def __init__(self):
        self.character = None
        self.monsters = {
            'Goblin': {'health': 30, 'attack_power': 5},
            'Troll': {'health': 50, 'attack_power': 10},
            'Dragon': {'health': 100, 'attack_power': 20}
        }

    def create_character(self):
        name = input("What is your character's name? ")
        char_type = input("Choose your class (Warrior, Mage, Archer): ")
        health = 100  # default health; can vary based on class
        attack_power = 20  # default attack power; can also vary based on class
        self.character = Character(name, char_type, health, attack_power)
        print(
            f"Character {self.character.name} the {self.character.char_type} is ready for adventure!")

    def spawn_monster(self):
        monster_type = random.choice(list(self.monsters.keys()))
        monster_info = self.monsters[monster_type]
        return Monster(monster_type, **monster_info)

    def main_loop(self):
        self.create_character()
        while self.character.is_alive():
            monster = self.spawn_monster()
            print(f"A wild {monster.species} appears!")
            action = input("Do you want to fight (f) or flee (r)? ")
            if action.lower() == 'f':
                self.character.battle(monster)
                if not self.character.is_alive():
                    print("Game Over")
                    break
            else:
                print(
                    f"{self.character.name} runs away from the {monster.species}!")
                continue  # Skip the rest of the loop and spawn a new monster

        print("Thank you for playing!")