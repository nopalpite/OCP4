class Player:
    """Player class"""

    def __init__(self, first_name, last_name, birth_date, gender, elo, id=0, score=0, have_played_with=[]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.elo = elo
        self.score = score
        self.have_played_with = have_played_with

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return self.id, self.last_name, self.first_name, self.gender, self.birth_date, self.elo

    def serialized(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'birth_date': self.birth_date,
                'gender': self.gender,
                'elo': self.elo,
                'score': self.score,
                'have_played_with': [x.id for x in self.have_played_with]
                }
