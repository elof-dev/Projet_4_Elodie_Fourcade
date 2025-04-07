import re
import datetime


class Player:
    def __init__(self, last_name, first_name, birthdate, chess_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.chess_id = chess_id

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthdate": self.birthdate,
            "chess_id": self.chess_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birthdate=data["birthdate"],
            chess_id=data["chess_id"]
        )


def validate_name(name):
    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[ '][A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    return bool(re.fullmatch(pattern, name))


def validate_birthdate(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        current_date = datetime.datetime.now()
        return date < current_date
    except ValueError:
        return False


def validate_chess_id(chess_id):
    pattern = r"^[A-Za-z]{2}\d{5}$"
    return bool(re.fullmatch(pattern, chess_id))
