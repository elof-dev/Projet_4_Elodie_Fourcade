class Match:
    def __init__(
        self, player1, player2, score1=0, score2=0, round_number=None
    ):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.round_number = round_number

    def to_dict(self):
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "score1": self.score1,
            "score2": self.score2,
            "round_number": self.round_number
        }

    @classmethod
    def from_dict(cls, data):
        from models.player import Player
        return cls(
            player1=Player.from_dict(data["player1"]),
            player2=Player.from_dict(data["player2"]),
            score1=data["score1"],
            score2=data["score2"],
            round_number=data.get("round_number")
        )
