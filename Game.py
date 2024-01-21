import random
from Character import Character 
from Monster import Monster 

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
        while True:
            char_type = input("Choose your class (Warrior, Mage, Archer): ")
            if char_type in Character.class_stats:
                break
            else:
                print("Invalid class. Please choose Warrior, Mage, or Archer.")
        self.character = Character(name, char_type)
        print(
            (f"Character {self.character.name} the " 
             f"{self.character.char_type} is ready for adventure!"))
        print((f"Health: {self.character.health}, " 
               f"Attack: {self.character.attack_power}"))

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
                    (f"{self.character.name} runs away from " 
                     f"the {monster.species}!"))

        print("Thank you for playing!")
