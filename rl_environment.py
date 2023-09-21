
import random
import json
from pet import Pet
from shop import Shop
from team import Team
from battle import Battle

class RLEnvironment:
    def __init__(self, pet_data):
        self.game = Game(pet_data)
        self.state = self.get_state()
        self.done = False

    def get_state(self):
        """Get the current state of the game."""
        state = self.game.get_game_state()
        simple_state = (
            tuple(state["shop"]["available_pets"]),
            tuple(state["player_team"]["pets"]),
            state["shop"]["gold"]
        )
        return simple_state

    def reset(self):
        """Reset the environment to start a new game."""
        self.game = Game(pet_data)
        self.state = self.get_state()
        self.done = False
        return self.state

    def step(self, action):
        """Take an action and return the next state, reward, and if the game is done."""
        if action == 0 and len(self.game.shop.available_pets) > 0:
            pet_index = random.randint(0, len(self.game.shop.available_pets) - 1)
            self.game.shop.buy_pet(pet_index, self.game.player_team)
        elif action == 1 and len(self.game.shop.items) > 0:
            item_index = random.randint(0, len(self.game.shop.items) - 1)
            pet = random.choice(self.game.player_team.get_pets())
            self.game.shop.buy_item(item_index, pet)
        elif action == 2:
            self.game.shop.roll()
        elif action == 3:
            self.game.simulate_opponent_buy_phase()
            self.game.play_battle_phase()
            winner = self.game.get_battle_winner()
            reward = 1 if winner == "Player" else -1
            self.done = True
            return self.get_state(), reward, self.done
        
        reward = 0
        return self.get_state(), reward, self.done
