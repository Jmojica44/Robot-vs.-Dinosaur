from robot import Robot
from dinosaur import Dinosaur

class Battlefield():
    def __init__(self):
        self.robot = Robot("Wall-e")
        self.dinosaur = Dinosaur("T-rex",15)
   
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print(f'Welcome to the arena!')
    
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health <= 0:
                break
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                break
    
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} has won the fight!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} has won the fight!')
