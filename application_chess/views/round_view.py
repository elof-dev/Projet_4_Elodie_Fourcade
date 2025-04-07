from views.match_view import MatchView


class RoundView:
    def __init__(self):
        self.match_view = MatchView()

    def display_round_message(self, message):
        print(message)

    def display_round(self, round_):
        print(f"\nRound {round_.number} :")
        for i, match in enumerate(round_.matches, 1):
            self.match_view.display_match(match, match_number=i)
