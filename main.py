from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from battlefield import Battlefield

robot_1 = Robot("Wall-e")
weapon_1 = Weapon("Excalibur",20)
dinosaur_1 = Dinosaur("T-rex",15)

while robot_1.health > 0 and dinosaur_1.health > 0:
    robot_1.attack(dinosaur_1)
    if dinosaur_1.health <= 0:
          break
    dinosaur_1.attack(robot_1)
if robot_1.health <= 0:
        print(f'{dinosaur_1.name} has won the fight!')
elif dinosaur_1.health <= 0:
     print(f'{robot_1.name} has won the fight!')


