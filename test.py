from game import Game
from pet import Pet
from team import Team
from shop import Shop
import json

# Loading the pet data
with open("pet_stats.json", "r") as read_file:
    pet_data = json.load(read_file)

def battle_phase(game):
    """Handle the battle phase of the game."""
    # Simulate the opponent's buy phase
    game.simulate_opponent_buy_phase()
    
    # Play the battle phase
    game.play_battle_phase()
    
    # Display the battle results
    winner = game.get_battle_winner()
    if winner:
        print(f"\n{winner} wins the battle!")
    else:
        print("\nThe battle is a tie!")

def interactive_simulation():
    """Run an interactive simulation of the game."""
    game = Game(pet_data)
    
    while True:
        print("\n" + "="*30)
        print(f"ROUND {game.rounds}")
        print("="*30)
        
        # Display the current state
        print("\nYOUR TEAM:")
        Team.display_team(game.player_team)
        print("\nSHOP:")
        game.shop.display()
        
        # Ask the user for their decision
        decision = input("\nWhat would you like to do? (buy_pet/buy_item/roll/end): ").strip().lower()
        
        if decision == "buy_pet" and len(game.shop.available_pets) > 0:
            pet_index = int(input(f"Which pet would you like to buy (0-{len(game.shop.available_pets)-1})? "))
            game.shop.buy_pet(pet_index, game.player_team)
        elif decision == "buy_item" and len(game.shop.items) > 0:
            item_index = int(input(f"Which item would you like to buy (0-{len(game.shop.items)-1})? "))
            pet_index = int(input(f"Which pet would you like to give the item to (0-{len(game.player_team.get_pets())-1})? "))
            game.shop.buy_item(item_index, game.player_team.get_pets()[pet_index])
        elif decision == "roll":
            game.shop.roll()
        elif decision == "end":
            break

    # Once the buy phase is over, proceed to the battle phase
    battle_phase(game)

    # Ask the user if they want to play another round
    continue_game = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if continue_game == "yes":
        game.start_new_round()
        interactive_simulation()

# Run the interactive simulation (this function is for demonstration purposes and won't be executed here)
interactive_simulation()
