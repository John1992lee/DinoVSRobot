

class Dinosaur:
    
    def __init__(self, name, power):
        self.name = name
        self.health = 150
        self.attack_power = power
        pass

    def attack(self, robot):
        robot.health -= self.attack_power
        pass