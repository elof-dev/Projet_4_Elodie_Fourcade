from views.match_view import MatchView


class TournamentView:
    def __init__(self):
        self.match_view = MatchView()

    def prompt_for_input(self, message):
        return input(message)

    def display_tournament_message(self, message):
        print(message)

    def display_tournament_created(self, tournament):
        print(f"\nTournoi '{tournament.name}' créé avec succès !")
        print(f"Lieu : {tournament.location}")
        print(f"Date de début : {tournament.start_time}")

    def display_tournament_finished(self, tournament):
        print(f"\nTournoi '{tournament.name}' terminé !")
        print(f"Date de fin : {tournament.end_time}")

    def display_tournaments(self, tournaments):
        print("\nTournois enregistrés :")
        for i, tournament in enumerate(tournaments, 1):
            print(f"{i}. {tournament.name} - {tournament.location}")

    def display_tournament_details(self, tournament):
        print(f"\nDétails du tournoi '{tournament.name}' :")
        print(f"Lieu : {tournament.location}")
        print(f"Date de début : {tournament.start_time}")
        print(f"Date de fin : {tournament.end_time}")
        print(f"Description : {tournament.description}")

        print("\nJoueurs (par ordre alphabétique) :")
        players_with_scores = sorted(
            tournament.get_players_with_scores(),
            key=lambda player_with_score: player_with_score[0].last_name
        )
        for player, score in players_with_scores:
            print(f"{player.last_name} {player.first_name} (Score : {score})")

        print("\nRounds :")
        for round_ in tournament.rounds:
            print(f"\nRound {round_.number} :")
            for i, match in enumerate(round_.matches, 1):
                self.match_view.display_match(match, match_number=i)
