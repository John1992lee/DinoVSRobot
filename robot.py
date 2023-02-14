from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = ""
        
        pass

    def attack(self, dinosaur):
        print(f'{self.name} is making an attack!')
        print()
        bool = True
        while bool == True:
            self.weapon_list = input(f"Which weapon would {self.name} like to attack with? Flamethrower, Rail Gun, or Chainsaw: ")
            if self.weapon_list == "Flamethrower":
                self.active_weapon = Weapon("Flamethrower", 20)
                bool = False
            elif self.weapon_list == "Rail Gun":
                self.active_weapon = Weapon("Rail Gun", 10)
                bool = False
            elif self.weapon_list == "Chainsaw":
                self.active_weapon = Weapon("Chainsaw", 5)
                bool = False
            else:
                print("That's not one of the list!")
            dinosaur.health -= self.active_weapon.attack_power
            
        pass
        

