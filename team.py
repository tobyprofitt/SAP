"""
Class to define a team of 5 (nullable) pets
"""

from pet import Pet 

class Team:
    def __init__(self, p1=None, p2=None, p3=None, p4=None, p5=None):
        self.p1 = Pet() if p1 is None else Pet(p1)
        self.p2 = Pet() if p2 is None else Pet(p2)
        self.p3 = Pet() if p3 is None else Pet(p3)
        self.p4 = Pet() if p4 is None else Pet(p4)
        self.p5 = Pet() if p5 is None else Pet(p5)
    
    def get_pets(self):
        return [self.p1, self.p2, self.p3, self.p4, self.p5]

    def __str__(self):
        return "Your pets are: {}, {}, {}, {}, and {}, reverse order for battling".format(self.p1, self.p2, self.p3, self.p4, self.p5)
    
    def is_alive(self):
        pets = self.get_pets()
        for pet in pets:
            if pet.is_alive():
                return True
        return False
    
    def get_front_pet(self):
        pets = self.get_pets()
        for pet in pets:
            if pet.is_alive():
                return pet
    
    def add_pet(self, new_pet):
        """
        Add a new pet to the team in the first empty slot.
        """
        if self.p1.name is None:
            self.p1 = new_pet
        elif self.p2.name is None:
            self.p2 = new_pet
        elif self.p3.name is None:
            self.p3 = new_pet
        elif self.p4.name is None:
            self.p4 = new_pet
        elif self.p5.name is None:
            self.p5 = new_pet
        else:
            print("No empty slots available to add a new pet.")
