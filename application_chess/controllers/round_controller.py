import random
from models.round import Round
from models.match import Match
from views.round_view import RoundView
from controllers.match_controller import MatchController


class RoundController:
    def __init__(self, save_tournament_callback):
        self.view = RoundView()
        self.match_controller = MatchController(save_tournament_callback)

    def create_first_round(self, players):
        self.view.display_round_message("Création du premier round...")
        random.shuffle(players)
        matches = []
        for i in range(0, len(players) - 1, 2):
            matches.append(Match(players[i], players[i + 1], round_number=1))
        return Round(1, matches)

    def create_next_round(self, tournament):
        players = sorted(
            tournament.get_players_with_scores(),
            key=lambda ranked_player: (
                -ranked_player[1], ranked_player[0].last_name
                )
        )
        matches = []
        used_players = set()
        for player_index in range(len(players)):
            if players[player_index][0] in used_players:
                continue
            for opponent_index in range(player_index + 1, len(players)):
                if (
                    players[opponent_index][0] not in used_players
                    and not tournament.has_played(
                        players[player_index][0], players[opponent_index][0]
                    )
                ):
                    matches.append(
                        Match(
                            players[player_index][0],
                            players[opponent_index][0],
                            round_number=len(tournament.rounds) + 1
                        )
                    )
                    used_players.add(players[player_index][0])
                    used_players.add(players[opponent_index][0])
                    break
        return Round(len(tournament.rounds) + 1, matches)

    def play_round(self, round_, tournament):
        self.view.display_round(round_)
        for match in round_.matches:
            self.match_controller.play_match(match, tournament)
        round_.end_round()

    def resume_round(self, tournament):
        while True:
            active_round = next(
                (
                    round_ for round_ in tournament.rounds
                    if not round_.end_time
                ),
                None
            )
            if active_round:
                self.play_round(active_round, tournament)
            else:
                if len(tournament.rounds) < 4:
                    new_round = self.create_next_round(tournament)
                    tournament.rounds.append(new_round)
                    self.play_round(new_round, tournament)
                else:
                    self.view.display_round_message("Le tournoi est terminé.")
                    break
