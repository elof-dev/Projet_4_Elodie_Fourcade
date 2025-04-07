class PlayerView:
    def prompt_for_input(self, message):
        return input(message)

    def display_player_message(self, message):
        print(message)

    def display_players(self, players):
        print("\nListe des joueurs :")
        for player in players:
            print(f"{player.last_name} {player.first_name} - "
                  f"Date de naissance : {player.birthdate},"
                  f" chess_ID : {player.chess_id}")
