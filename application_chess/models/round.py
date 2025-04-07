import datetime


class Round:
    def __init__(self, number, matches):
        self.number = number
        self.matches = matches
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        self.end_time = None

    def end_round(self):
        self.end_time = datetime.datetime.now().replace(microsecond=0)

    def to_dict(self):
        return {
            "number": self.number,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": (
                self.end_time.strftime("%Y-%m-%d %H:%M:%S")
                if self.end_time
                else None
            )
        }

    @classmethod
    def from_dict(cls, data):
        from models.match import Match
        round_ = cls(
            number=data["number"],
            matches=[Match.from_dict(match) for match in data["matches"]]
        )
        round_.start_time = datetime.datetime.strptime(
            data["start_time"], "%Y-%m-%d %H:%M:%S"
        )
        round_.end_time = (
            datetime.datetime.strptime(data["end_time"], "%Y-%m-%d %H:%M:%S")
            if data["end_time"]
            else None
        )
        return round_
