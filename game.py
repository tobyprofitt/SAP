from shop import Shop
from team import Team
from battle import Battle
from pet import Pet
import random
import json

# Loading the pet data
with open("pet_stats.json", "r") as read_file:
    pet_data = json.load(read_file)

class Game:
    def __init__(self, pet_data):
        self.pet_data = pet_data
        self.shop = Shop(self.pet_data)
        self.player_team = Team()
        self.opponent_team = Team()
        self.rounds = 1
        self.battle = None

    def start_new_round(self):
        self.rounds += 1
        self.shop.initialize_shop()

    def simulate_opponent_buy_phase(self):
        # A simple strategy for the opponent to buy pets and items
        while self.shop.gold > 0:
            action = random.choice(["buy_pet", "buy_item", "roll"])
            if action == "buy_pet" and len(self.shop.available_pets) > 0:
                pet_index = random.randint(0, len(self.shop.available_pets) - 1)
                self.shop.buy_pet(pet_index, self.opponent_team)
            elif action == "buy_item" and len(self.shop.items) > 0:
                item_index = random.randint(0, len(self.shop.items) - 1)
                pet = random.choice(self.opponent_team.get_pets())
                self.shop.buy_item(item_index, pet)
            elif action == "roll":
                self.shop.roll()

    def play_battle_phase(self):
        self.battle = Battle(self.player_team, self.opponent_team)
        self.battle.start_battle()
        while not self.battle.is_battle_over():
            self.battle.take_turn()

    def get_game_state(self):
        state = {
            "round": self.rounds,
            "shop": self.shop.get_state(),
            "player_team": self.player_team.get_state(),
            "opponent_team": self.opponent_team.get_state()
        }
        return state

    def get_battle_winner(self):
        return self.battle.get_winner()