class Dinosaur():
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    def attack(self, robot):
        damage = self.attack_power
        robot.health -= self.attack_power
        print(f' Dinosaur attacks {robot.name}.')
        print(f' {robot.name} takes {damage} points of damage and now has {robot.health} left.')
        
