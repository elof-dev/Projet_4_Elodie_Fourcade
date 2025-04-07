import datetime


class Tournament:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        self.rounds = []
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        self.end_time = None

    def end_tournament(self):
        self.end_time = datetime.datetime.now().replace(microsecond=0)

    def add_round(self, round_):
        self.rounds.append(round_)

    def get_players_with_scores(self):
        players = {}
        for round_ in self.rounds:
            for match in round_.matches:
                if match.player1.chess_id not in players:
                    players[match.player1.chess_id] = {
                        "player": match.player1,
                        "score": 0
                    }
                if match.player2.chess_id not in players:
                    players[match.player2.chess_id] = {
                        "player": match.player2,
                        "score": 0
                    }
                players[match.player1.chess_id]["score"] += match.score1
                players[match.player2.chess_id]["score"] += match.score2

        return sorted(
            [(data["player"], data["score"]) for data in players.values()],
            key=lambda sorted_player_data: sorted_player_data[0].last_name
        )

    def has_played(self, player1, player2):
        for round_ in self.rounds:
            for match in round_.matches:
                if (match.player1 == player1 and match.player2 == player2) or \
                   (match.player1 == player2 and match.player2 == player1):
                    return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": (
                self.end_time.strftime("%Y-%m-%d %H:%M:%S")
                if self.end_time else None
            )
        }

    @classmethod
    def from_dict(cls, data):
        from models.round import Round
        tournament = cls(
            name=data["name"],
            location=data["location"],
            description=data["description"]
        )
        tournament.rounds = [
            Round.from_dict(round_) for round_ in data["rounds"]
        ]
        tournament.start_time = datetime.datetime.strptime(
            data["start_time"], "%Y-%m-%d %H:%M:%S"
        )
        tournament.end_time = (
            datetime.datetime.strptime(data["end_time"], "%Y-%m-%d %H:%M:%S")
            if data["end_time"]
            else None
        )
        return tournament
