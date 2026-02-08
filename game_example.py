class SecureGameEngine:
    def __init__(self):
        self.players = {}

    def add_player(self, player_id):
        self.players[player_id] = {'hp': 100, 'gold': 0, 'level': 1}

    def update_hp(self, player_id, amount):
        if player_id in self.players:
            self.players[player_id]['hp'] += amount

    def earn_gold(self, player_id, amount):
        if player_id in self.players:
            self.players[player_id]['gold'] += amount

    def level_up(self, player_id):
        if player_id in self.players:
            self.players[player_id]['level'] += 1

    def display_player_info(self, player_id):
        if player_id in self.players:
            player_info = self.players[player_id]
            print(f"Player: {player_id}, HP: {player_info['hp']}, Gold: {player_info['gold']}, Level: {player_info['level']}")

# Example Usage
if __name__ == "__main__":
    game = SecureGameEngine()
    game.add_player('Player1')
    game.earn_gold('Player1', 50)
    game.update_hp('Player1', -10)
    game.level_up('Player1')
    game.display_player_info('Player1')
