from random import shuffle


class Match:
    """Match class"""

    def __init__(self,
                 id,
                 players,
                 player1_color="",
                 player2_color="",
                 player1_score=0,
                 player2_score=0,
                 is_complete=False):
        self.id = id
        self.player1 = players[0]
        self.player2 = players[1]
        self.player1_color = player1_color
        self.player2_color = player2_color
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.is_complete = is_complete

    def __repr__(self):
        return f"'{self.player1}'[{self.player1_score}] " \
                f"'{self.player2}'[{self.player2_score}]\n"

    def __str__(self):
        return f"{self.player1.last_name} {self.player1.first_name} VS {self.player2.last_name}" \
               f" {self.player2.first_name} "

    def serialized(self):
        return {'id': self.id,
                'players': [self.player1.id, self.player2.id],
                'player1_color': self.player1_color,
                'player2_color': self.player2_color,
                'player1_score': self.player1_score,
                'player2_score': self.player2_score,
                'is_complete': self.is_complete}

    def set_players_color(self):
        colors = ["Blanc", "Noir"]
        shuffle(colors)
        self.player1_color = colors[0]
        self.player2_color = colors[1]

    def play(self, player1_score, player2_score):
        self.set_players_color()
        self.player1.score += player1_score
        self.player2.score += player2_score
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.player1.have_played_with.append(self.player2)
        self.player2.have_played_with.append(self.player1)
        self.is_complete = True
