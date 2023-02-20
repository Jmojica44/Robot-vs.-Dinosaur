from weapon import Weapon

class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Excalibur", 20)
    def attack(self, dinosaur):
        damage = self.active_weapon.attack_power
        dinosaur.health -= damage
        print(f' {self.name} attacks {dinosaur.name}.')
        print(f' {dinosaur.name} takes {damage} points of damage and now has {dinosaur.health} health left.')


#active weapon is an instantiation of the weapon class
