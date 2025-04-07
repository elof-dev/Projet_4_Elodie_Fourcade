import os
from models.player import (
    Player,
    validate_name,
    validate_birthdate,
    validate_chess_id,
)
from views.player_view import PlayerView
from utils import ensure_file_exists, load_json, save_json


class PlayerController:
    def __init__(self, data_file=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = data_file or os.path.join(
            base_dir, "..", "data", "players.json")
        self.view = PlayerView()
        ensure_file_exists(self.data_file)

    def load_players(self):
        return [Player(**data) for data in load_json(self.data_file)]

    def save_players(self, players):
        save_json(self.data_file, [player.to_dict() for player in players])

    def prompt_and_validate(
        self, prompt_message, validation_function, error_message
    ):
        while True:
            value = self.view.prompt_for_input(prompt_message)
            if validation_function(value):
                return value
            self.view.display_player_message(error_message)

    def create_player(self):
        last_name = self.prompt_and_validate(
            "Nom : ",
            validate_name,
            "Nom invalide. Veuillez réessayer."
            )
        first_name = self.prompt_and_validate(
            "Prénom : ",
            validate_name,
            "Prénom invalide. Veuillez réessayer."
            )
        birthdate = self.prompt_and_validate(
            "Date de naissance (JJ/MM/AAAA) : ",
            validate_birthdate,
            "Date de naissance invalide. Veuillez réessayer."
            )
        chess_id = self.prompt_and_validate(
                "ID d'échecs (ex : AB12345) : ",
                validate_chess_id,
                "ID d'échecs invalide. Veuillez réessayer."
            )

        players = self.load_players()
        players.append(Player(last_name, first_name, birthdate, chess_id))
        self.save_players(players)
        self.view.display_player_message("Joueur créé avec succès.")

    def display_players(self):
        players = self.load_players()
        if not players:
            self.view.display_player_message("Aucun joueur enregistré.")
            return

        sorted_players = sorted(
            players, key=lambda player: (player.last_name, player.first_name))
        self.view.display_players(sorted_players)
