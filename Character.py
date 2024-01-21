# Re-writing the modified Character class after the reset.

class Character:
    BASE_HEALTH = 100
    BASE_ATTACK = 10

    class_stats = {
        'Warrior': {'health': 120, 'attack': 15},
        'Mage': {'health': 80, 'attack': 25},
        'Archer': {'health': 100, 'attack': 20}
    }

    def __init__(self, name, char_type):
        self.name = name
        self.char_type = char_type
        self.health = \
            self.BASE_HEALTH + (
                self.class_stats[char_type]['health'] 
                if char_type in self.class_stats else 0)
        self.attack_power = \
            self.BASE_ATTACK + (
                self.class_stats[char_type]['attack'] 
                if char_type in self.class_stats else 0)

    def attack(self, target):
        target.health -= self.attack_power
        print((f"{self.name} attacks {target.species} "
                 f"for {self.attack_power} damage."))

    def is_alive(self):
        return self.health > 0

    def battle(self, monster):
        # Simple turn-based battle logic where the character and monster
        # take turns attacking each other
        while self.is_alive() and monster.is_alive():
            self.attack(monster)
            if monster.is_alive():
                monster.attack(self)
        
        if self.is_alive():
            print(f"{self.name} defeated the {monster.species}!")
        else:
            print(f"{self.name} was defeated by the {monster.species}.")
