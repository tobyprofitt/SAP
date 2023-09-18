
import random

class Shop:
    def __init__(self, pet_data):
        self.gold = 10
        self.pet_data = pet_data
        self.available_pets = []
        self.items = ["Shield", "Sword", "Armor"]
        self.initialize_shop()

    def initialize_shop(self):
        pet_ids = list(self.pet_data.keys())
        selected_pet_ids = random.sample(pet_ids, 5)
        for pet_id in selected_pet_ids:
            pet_info = self.pet_data[pet_id]
            pet = Pet(name=pet_info["Name"], attack=pet_info["Attack"], health=pet_info["Health"], tier=pet_info["Tier"], trigger=pet_info["Trigger"])
            self.available_pets.append(pet)

    def get_state(self):
        state = {
            "gold": self.gold,
            "available_pets": [(pet.name, pet.get_attack(), pet.get_health(), pet.tier, pet.get_trigger()) for pet in self.available_pets],
            "available_items": self.items.copy()
        }
        return state

    def buy_pet(self, pet_index, team):
        if self.gold >= 3:
            pet = self.available_pets.pop(pet_index)
            team.add_pet(pet)
            self.gold -= 3

    def buy_item(self, item_index, pet):
        if self.gold >= 3:
            item = self.items.pop(item_index)
            pet.set_item(item)
            self.gold -= 3

    def roll(self):
        if self.gold >= 1:
            self.available_pets = []
            self.items = ["Shield", "Sword", "Armor"]
            self.initialize_shop()
            self.gold -= 1
