
class Battle:
    def __init__(self, player_team, opponent_team):
        self.player_team = player_team
        self.opponent_team = opponent_team
        self.current_turn = "player"

    def start_battle(self):
        self.player_team.reset_team()
        self.opponent_team.reset_team()
        self.current_turn = "player"

    def take_turn(self):
        player_pet = self.player_team.get_next_pet()
        opponent_pet = self.opponent_team.get_next_pet()

        if self.current_turn == "player":
            if player_pet and opponent_pet:
                opponent_pet.take_damage(player_pet.get_attack())
                self.current_turn = "opponent"
        else:
            if player_pet and opponent_pet:
                player_pet.take_damage(opponent_pet.get_attack())
                self.current_turn = "player"

    def get_winner(self):
        if not self.player_team.has_available_pet():
            return "opponent"
        elif not self.opponent_team.has_available_pet():
            return "player"
        else:
            return None

    def is_battle_over(self):
        return not self.player_team.has_available_pet() or not self.opponent_team.has_available_pet()
