from datetime import datetime
from models.player import Player
from models.match import Match


class Round:

    def __init__(self, id, name, players):
        self.id = id
        self.name = name
        self.players = players
        self.paired_players = []
        self.matches = []
        self.start_time = "pas encore commencé"
        self.end_time = "pas encore terminé"
        self.is_complete = False
        self.is_started = False

    def __str__(self):
        return f"{self.name} heure de début: {self.start_time} heure de fin: {self.end_time}"

    def __repr__(self):
        return self.name, self.start_time, self.end_time, self.matches

    def is_first_round(self):
        total_score = 0
        for player in self.players:
            total_score += player.score
        if total_score == 0:
            return True

    def pair_players(self):
        middle_index = len(self.players) // 2
        paired_players = []
        if self.is_first_round():
            self.players.sort(key=lambda x: x.elo, reverse=True)
            top_list = self.players[:middle_index]
            bottom_list = self.players[middle_index:]
            for player1, player2 in zip(top_list, bottom_list):
                paired_players.append([player1, player2])
        else:
            self.players.sort(key=lambda x: (x.score, x.elo), reverse=True)
            source = self.players.copy()
            target = []
            index = 1
            while len(source) > 2:
                print("index: " + str(index) + "source: " + str(len(source)))
                if not source[index] in source[0].have_played_with:
                    target.append([source[0], source[index]])
                    del source[index]
                    del source[0]
                    index = 1
                elif index == len(source) - 1:
                    target.append([source[0], source[index]])
                    del source[index]
                    del source[0]
                else:
                    index += 1

            target.append([source[0], source[1]])
            del source
            paired_players = target
        return paired_players

    def create_matches(self):
        matches = []
        index = 1
        for i in self.paired_players:
            matches.append(Match(index, i))
            index += 1
        return matches

    def start(self):
        if not self.is_started:
            print("starting round")
            self.start_time = datetime.now()
            self.paired_players = self.pair_players()
            self.matches = self.create_matches()
            self.is_started = True

    def complete(self):
        self.end_time = datetime.now()
        self.is_complete = True

    def report(self):
        return [f"Nom: {self.name}",
                f"Heure de début: {self.start_time}",
                f"Heure de fin: {self.date}",
                f"Nombres de matchs: {len(self.matches)}",
                ]
