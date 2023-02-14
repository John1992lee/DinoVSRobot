from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.robot = Robot("Instant Death 2000")
        self.dinosaur = Dinosaur("Tracytop", 20)
        pass

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass

    def display_welcome(self):
        print()
        print("Welcome to the battle of the Century, Robot vs Dino!")
        print()
        print(self.dinosaur.name, "was eating his meal until", self.robot.name, "decided to attack!")
        pass

    def battle_phase(self):
        while True:
            self.robot.attack(self.dinosaur)
            print()
            print(self.robot.name, "has attack", self.dinosaur.name, "with a", self.robot.active_weapon.name, "and dealth", self.robot.active_weapon.attack_power, "damage!")
            print(self.dinosaur.name, "has", self.dinosaur.health, "health left!")
            print()
            self.dinosaur.attack(self.robot)
            print(self.dinosaur.name, "has attack", self.robot.name, "and dealth", self.dinosaur.attack_power, "damage!")
            print(self.robot.name, "has", self.robot.health, "health left!")
            print()
            if self.dinosaur.health <= 0 or self.robot.health <= 0:
                break
        pass

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(self.dinosaur.name, "became ancient barbeque!")
            print(self.robot.name, "is the Winner of the century!")
        elif self.robot.health <= 0:
            print(self.robot.name, "went up in smokes!")
            print()
            print(self.dinosaur.name, "has win the battle of the century!")
        pass

