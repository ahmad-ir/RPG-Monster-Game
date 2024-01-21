class Monster:

    def __init__(self, species, health, attack_power):
        self.species = species
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(
            (f"The {self.species} attacks {target.name} for " 
             f"{self.attack_power} damage."))

    def is_alive(self):
        return self.health > 0