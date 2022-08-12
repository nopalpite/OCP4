
class Player:

    def __init__(self, first_name, last_name, birth_date, gender, elo):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.elo = elo
        self.score = 0
        self.have_played_with = []
        self.id = 0

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return self.id, self.last_name, self.first_name, self.gender, self.birth_date, self.elo

