class Monster:

    def __init__(self, species, health, attack_power):
        self.species = species
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(
            f"The {self.species} attacks {target.name} for {self.attack_power} damage.")

    def is_alive(self):
        return self.health > 0

# Commenting out the instantiation of the class, since we're just setting up the structure.
# monster_example = Monster("Goblin", 30, 5)