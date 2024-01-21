import random
from Character import Character 
from Monster import Monster 
import pickle


class Game:
    def __init__(self):
        self.character = None
        self.monsters = {
            'Goblin': {'health': 30, 'attack_power': 5},
            'Troll': {'health': 50, 'attack_power': 10},
            'Dragon': {'health': 100, 'attack_power': 20}
        }

    def save_game(self):
        with open('game_save.pkl', 'wb') as file:
            pickle.dump(self, file)
        print("Game saved successfully.")

    def load_game(self):
        try:
            with open('game_save.pkl', 'rb') as file:
                loaded_game = pickle.load(file)
            print("Game loaded successfully.")
            return loaded_game
        except FileNotFoundError:
            print("No saved game found.")
            return None

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

        # Check if the user wants to load a saved game
        load_choice = input("Do you want to continue a saved game? (yes/no): ")
        if load_choice.lower() == 'yes':
            loaded_game = self.load_game()
            if loaded_game:
                self = loaded_game
            else:
                print("Starting a new game.")
                self.create_character()
        else:
            self.create_character()

        while self.character.is_alive():
            monster = self.spawn_monster()
            print(f"A wild {monster.species} appears!")
            action = input(
                "Do you want to fight (f), flee (r), or save the game (s)? ")
            if action.lower() == 'f':
                self.character.battle(monster)
                if not self.character.is_alive():
                    print("Game Over")
                    break
            elif action.lower() == 'r':
                print(
                    (f"{self.character.name} runs away from " 
                     f" the {monster.species}!"))
            elif action.lower() == 's':
                self.save_game()

        print("Thank you for playing!")
