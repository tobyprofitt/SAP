
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

    def get_state(self):
        state = {
            "pets": [(pet.name, pet.get_attack(), pet.get_health(), pet.tier, pet.get_trigger(), pet.get_item()) for pet in self.get_pets()]
        }
        return state

    def add_pet(self, pet):
        pets = self.get_pets()
        for i, existing_pet in enumerate(pets):
            if existing_pet.name == "Unnamed":
                pets[i] = pet
                break

    def get_next_pet(self):
        pets = self.get_pets()
        for pet in pets:
            if pet.is_alive():
                return pet
        return None

    def has_available_pet(self):
        pets = self.get_pets()
        for pet in pets:
            if pet.is_alive():
                return True
        return False

    def reset_team(self):
        pets = self.get_pets()
        for pet in pets:
            pet.reset_pet()

    def display_team(team):
        """Display the details of the pets in the given team."""
        if not team.get_pets():
            print("Your team is empty!")
            return
        
        for i, pet in enumerate(team.get_pets()):
            print(f"Pet {i + 1}:")
            print(f"  Name: {pet.name}")
            print(f"  Attack: {pet.get_attack()}")
            print(f"  HP: {pet.get_health()}")
            if pet.item:
                print(f"  Item: {pet.item.name} ({pet.item.description})")
            else:
                print("  No item equipped.")
