class Character:

    def __init__(self, name, char_type, health, attack_power):
        self.name = name
        self.char_type = char_type
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(
            f"{self.name} attacks {target.species} for {self.attack_power} damage.")

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

    # Also commenting out the battle invocation, since we're not running the
    # code at this moment.
    # hero = Character("Arin", "Warrior", 100, 20)
    # villain = Monster("Ogre", 80, 15)
    # hero.battle(villain)