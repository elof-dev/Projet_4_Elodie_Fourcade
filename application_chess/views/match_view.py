class MatchView:
    def format_match_info(self, match, match_number=None):
        match_info = (
            f"{match.player1.last_name} {match.player1.first_name} "
            f"({match.player1.chess_id}) VS "
            f"{match.player2.last_name} {match.player2.first_name} "
            f"({match.player2.chess_id})"
        )
        if match_number is not None:
            return f"Match {match_number} : {match_info}"
        return match_info

    def request_match_result(self, match, match_number=None):
        match_info = self.format_match_info(match, match_number)
        print(f"\n{match_info}")
        return input("Entrez le chess_id du gagnant ou 'match nul' : ")

    def display_match_message(self, message):
        print(message)

    def determine_match_winner(self, match):
        if match.score1 == 0 and match.score2 == 0:
            return "Résultat : En attente"
        elif match.score1 > match.score2:
            return (
                f"Gagnant : {match.player1.last_name} "
                f"{match.player1.first_name} (Score : {match.score1})"
            )
        elif match.score2 > match.score1:
            return (
                f"Gagnant : {match.player2.last_name} "
                f"{match.player2.first_name} (Score : {match.score2})"
            )
        else:
            return "Résultat : Match nul"

    def display_match(self, match, match_number=None):
        match_info = self.format_match_info(match, match_number)
        result = self.determine_match_winner(match)
        print(f"{match_info} - {result}")
