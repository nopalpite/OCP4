from datetime import datetime
from models.match import Match


class Round:

    def __init__(self, id, name, players, paired_players=[], matches=[], start_time="pas encore commencé",
                 end_time="pas encore terminé", is_complete=False, is_started=False):
        self.id = id
        self.name = name
        self.players = players
        self.paired_players = paired_players
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time
        self.is_complete = is_complete
        self.is_started = is_started

    def __str__(self):
        return f"{self.name} heure de début: {self.start_time} heure de fin: {self.end_time}"

    def __repr__(self):
        matches =  [match for match in self.matches if match.is_complete]
        return self.name, self.start_time, self.end_time, matches

    def serialized(self):
        return {'id': self.id,
                'name': self.name,
                'players': [x.id for x in self.players],
                'paired_players': [[x[0].id, x[1].id] for x in self.paired_players],
                'matches': [x.serialized() for x in self.matches],
                'start_time': self.start_time,
                'end_time': self.end_time,
                'is_complete': self.is_complete,
                'is_started': self.is_started
                }

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
            sorted_players = sorted(self.players, key=lambda x: x.elo, reverse=True)
            top_list = sorted_players[:middle_index]
            bottom_list = sorted_players[middle_index:]
            for player1, player2 in zip(top_list, bottom_list):
                paired_players.append([player1, player2])
        else:
            sorted_players = sorted(self.players, key=lambda x: (x.score, x.elo), reverse=True)
            source = sorted_players.copy()
            target = []
            index = 1
            while len(source) > 2:
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
            match = Match(index,i)
            matches.append(match)
            index += 1
        return matches

    def start(self):
        if not self.is_started:
            self.start_time = datetime.now().__str__()
            self.paired_players = self.pair_players()
            self.matches = self.create_matches()
            self.is_started = True

    def complete(self):
        self.end_time = datetime.now().__str__()
        self.is_complete = True

    def report(self):
        return [f"Nom: {self.name}",
                f"Heure de début: {self.start_time}",
                f"Heure de fin: {self.end_time}",
                f"Nombres de matchs: {len(self.matches)}",
                ]
