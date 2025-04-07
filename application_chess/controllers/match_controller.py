from views.match_view import MatchView


class MatchController:
    def __init__(self, save_tournament_callback):
        self.view = MatchView()
        self.save_tournament_callback = save_tournament_callback

    def play_match(self, match, tournament):
        # Vérifie si le match a déjà un résultat
        if match.score1 != 0 or match.score2 != 0:
            return

        while True:
            result = self.view.request_match_result(match)
            if result == match.player1.chess_id:
                match.score1 = 1
                match.score2 = 0
                break
            elif result == match.player2.chess_id:
                match.score1 = 0
                match.score2 = 1
                break
            elif result.lower() == "match nul":
                match.score1 = 0.5
                match.score2 = 0.5
                break
            else:
                self.view.display_match_message(
                    "Entrée invalide. Veuillez réessayer."
                    )
        # Mettre à jour le round dans le tournoi avant la sauvegarde
        for i, round_ in enumerate(tournament.rounds):
            if round_.number == match.round_number:
                tournament.rounds[i] = round_
                break

        # Sauvegarde du tournoi après chaque résultat
        self.save_tournament_callback(tournament)
