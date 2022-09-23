from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from controllers.controller import Controller


class DatabaseController(Controller):

    def __init__(self):
        super().__init__()

    # DATABASE #

    def load_players(self):
        players = self.db.players_table.all()
        for player in players:
            self.players_list.append(Player(**player))

    def load_player(self, id):
        for player in self.players_list:
            if player.id == id:
                return player

    def load_tournament_players(self, tournament):
        for player_data in self.db.tournaments_table.get(doc_id=tournament.id)["players"]:
            for player in self.players_list:
                if player.id == player_data["id"]:
                    player.score = player_data["score"]
                    player.have_played_with = [self.load_player(id) for id in player_data["have_played_with"]]

    def load_player_pairs(self, ids):
        output = []
        paired_players = [self.load_player(id) for id in ids]
        output.append(paired_players)
        return output

    def load_match(self, match):
        return Match(
            match["id"],
            [self.load_player(id) for id in match["players"]],
            match["player1_color"],
            match["player2_color"],
            match["player1_score"],
            match["player2_score"],
            match["is_complete"]
        )

    def load_round(self, round, tournament_data):
        output = Round(
            round["id"],
            round["name"],
            [self.load_player(player["id"]) for player in tournament_data],
            [[self.load_player(pair[0]), self.load_player(pair[1])] for pair in round["paired_players"]],
            [self.load_match(match) for match in round["matches"]],
            round["start_time"],
            round["end_time"],
            round["is_complete"],
            round["is_started"]
        )
        return output

    def load_tournaments(self):
        tournaments = self.db.tournaments_table.all()
        for tournament_data in tournaments:
            tournament = Tournament(
                tournament_data["name"],
                tournament_data["place"],
                [self.load_player(player["id"]) for player in tournament_data["players"]],
                tournament_data["time_control"],
                tournament_data["rounds_range"],
                tournament_data["description"],
                [self.load_round(round, tournament_data["players"]) for round in tournament_data["rounds"]],
                tournament_data["id"],
                tournament_data["start_date"],
                tournament_data["end_date"],
                tournament_data["is_started"],
                tournament_data["is_complete"]
            )
            self.tournaments_list.append(tournament)

    def load_db(self):
        self.load_players()
        self.load_tournaments()
