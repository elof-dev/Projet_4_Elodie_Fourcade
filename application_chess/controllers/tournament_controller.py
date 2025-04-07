import os
import random
from models.tournament import Tournament
from controllers.round_controller import RoundController
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController
from views.round_view import RoundView
from utils import ensure_file_exists, load_json, save_json


class TournamentController:
    def __init__(self, data_file=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = data_file or os.path.join(
            base_dir, "..", "data", "tournaments.json")
        self.view = TournamentView()
        self.round_view = RoundView()
        self.round_controller = RoundController(self.save_tournament)
        self.player_controller = PlayerController()
        ensure_file_exists(self.data_file)

    def load_tournaments(self):
        return [
            Tournament.from_dict(data)
            for data in load_json(self.data_file)
        ]

    def save_tournaments(self, tournaments):
        save_json(self.data_file, [tournament.to_dict()
                  for tournament in tournaments])

    def create_tournament(self):
        name = self.view.prompt_for_input("Nom du tournoi : ")
        location = self.view.prompt_for_input("Lieu du tournoi : ")
        description = self.view.prompt_for_input("Description du tournoi : ")

        tournament = Tournament(name, location, description)
        players = self.player_controller.load_players()

        if len(players) < 2:
            self.view.display_tournament_message(
                "Pas assez de joueurs pour créer un tournoi.")
            return

        random.shuffle(players)
        first_round = self.round_controller.create_first_round(players)
        tournament.add_round(first_round)
        self.save_tournament(tournament)

        self.view.display_tournament_created(tournament)
        self.round_controller.play_round(first_round, tournament)

        for i in range(2, 5):
            next_round = self.round_controller.create_next_round(tournament)
            tournament.add_round(next_round)
            self.save_tournament(tournament)
            self.round_controller.play_round(next_round, tournament)

        tournament.end_tournament()
        comment = self.view.prompt_for_input(
            "Souhaitez-vous ajouter un commentaire ? ")
        if comment:
            tournament.description += f"\nCommentaire : {comment}"
        self.save_tournament(tournament)
        self.view.display_tournament_finished(tournament)

    def resume_tournament(self):
        tournaments = self.load_tournaments()
        ongoing_tournaments = [
            ongoing_tournament
            for ongoing_tournament in tournaments
            if ongoing_tournament.end_time is None
        ]

        if not ongoing_tournaments:
            self.view.display_tournament_message(
                "Aucun tournoi en cours à reprendre."
                )
            return

        self.view.display_tournaments(ongoing_tournaments)
        choice = self.view.prompt_for_input(
            "Entrez le numéro du tournoi à reprendre : ")
        try:
            tournament = ongoing_tournaments[int(choice) - 1]
        except (IndexError, ValueError):
            self.view.display_tournament_message("Choix invalide.")
            return

        self.view.display_tournament_message("\nHistorique du tournoi :")
        for round_ in tournament.rounds:
            if round_.end_time:
                self.round_view.display_round(round_)

        self.round_controller.resume_round(tournament)
        self.save_tournament(tournament)
        tournament.end_tournament()
        comment = self.view.prompt_for_input(
            "Souhaitez-vous ajouter un commentaire ? ")
        if comment:
            tournament.description += f"\nCommentaire : {comment}"
        self.save_tournament(tournament)
        self.view.display_tournament_finished(tournament)

    def view_tournament_details(self):
        tournaments = self.load_tournaments()
        if not tournaments:
            self.view.display_tournament_message("Aucun tournoi enregistré.")
            return

        self.view.display_tournaments(tournaments)
        choice = self.view.prompt_for_input(
            "Entrez le numéro du tournoi à voir : ")
        try:
            tournament = tournaments[int(choice) - 1]
        except (IndexError, ValueError):
            self.view.display_tournament_message("Choix invalide.")
            return

        self.view.display_tournament_details(tournament)

    def save_tournament(self, tournament):
        tournaments = self.load_tournaments()
        for tournament_index, current_tournament in enumerate(tournaments):
            if (
                current_tournament.name == tournament.name
                and current_tournament.start_time == tournament.start_time
            ):
                tournaments[tournament_index] = tournament
                break
        else:
            tournaments.append(tournament)
        self.save_tournaments(tournaments)
