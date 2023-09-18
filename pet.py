
class Pet:
    def __init__(self, name="Unnamed", attack=0, health=0, tier=1, trigger="start_of_turn"):
        self.name = name
        self.base_attack = attack
        self.base_health = health
        self.tier = tier
        self.trigger = trigger
        self.current_health = health
        self.item = None

    def get_attack(self):
        attack_bonus = 0
        if self.item == "Sword":
            attack_bonus = 5
        return self.base_attack + attack_bonus

    def get_health(self):
        return self.current_health

    def get_trigger(self):
        return self.trigger

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def is_alive(self):
        return self.current_health > 0

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)

    def reset_pet(self):
        self.current_health = self.base_health
        self.item = None
