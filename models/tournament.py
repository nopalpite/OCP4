ROUNDS_RANGE = 4
from datetime import date
from models.round import Round


class Tournament:

    def __init__(self, name, place, players, time_control, rounds_range=ROUNDS_RANGE, description=""):
        self.name = name
        self.place = place
        self.rounds_range = rounds_range
        self.players = players
        self.time_control = time_control
        self.description = description
        self.rounds = []
        self.start_date = "Pas encore commencé"
        self.end_date = "Pas encore terminé"
        self.id = 0
        self.is_complete = False


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
        self.start_date = date(now)

    def complete(self):
        self.is_complete = True
        self.end_date = date(now)

