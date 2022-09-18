ROUNDS_RANGE = 4
from datetime import date
from models.round import Round


class Tournament:

    def __init__(self, name, place, players, time_control, rounds_range=ROUNDS_RANGE, description="",
                 rounds=[], id=0, start_date="Pas encore commencé", end_date="Pas encore terminé",
                 is_started=False, is_complete=False):
        self.name = name
        self.place = place
        self.rounds_range = rounds_range
        self.players = players
        self.time_control = time_control
        self.description = description
        self.rounds = rounds
        self.start_date = start_date
        self.end_date = end_date
        self.id = id
        self.is_started = is_started
        self.is_complete = is_complete

    def serialized(self):
        return {'name': self.name,
                'place': self.place,
                'players': [x.serialized() for x in self.players],
                'time_control': self.time_control,
                'rounds_range': self.rounds_range,
                'description': self.description,
                'rounds': [x.serialized() for x in self.rounds],
                'id': self.id,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'is_started': self.is_started,
                'is_complete': self.is_complete
                }

    def __str__(self):
        return f"Tournoi: {self.name}"

    def __repr__(self):
        return self.id, self.name, self.place, self.start_date, self.end_date, self.description

    def create_rounds(self):
        round_number = 1
        for i in range(self.rounds_range):
            round = Round(round_number, "Round " + str(round_number), self.players)
            self.rounds.append(round)
            round_number += 1

    def start(self):
        self.create_rounds()
        self.start_date = date.today().__str__()
        self.is_started = True

    def complete(self):
        self.is_complete = True
        self.end_date = date.today().__str__()



