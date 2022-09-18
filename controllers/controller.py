from views.menu import MenuView
from views.reports import ReportsView
from views.error import ErrorView
from views.view import View
from models.player import Player
from models.round import Round
from models.match import Match
from models.tournament import Tournament
from controllers.database import Database

PLAYERS_RANGE = 8


class Controller:

    def __init__(self):
        self.view = View()
        self.menu_view = MenuView()
        self.reports_view = ReportsView()
        self.error_view = ErrorView()
        self.players = []
        self.tournaments = []
        self.db = Database()

    # DATABASE #

    def load_players(self):
        players = self.db.players_table.all()
        for player in players:
            self.players.append(Player(**player))

    def load_player(self, id):
        for player in self.players:
            if player.id == id:
                return player

    def load_tournament_players(self, tournament):
        for player_data in self.db.tournaments_table.get(doc_id=tournament.id)["players"]:
            for player in self.players:
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
            self.tournaments.append(tournament)

    # MENUS #

    def main_menu(self):
        choice = self.menu_view.main_menu()
        if choice == "1":
            self.create_tournament()
        elif choice == "2":
            self.create_player()
        elif choice == "3":
            self.load_tournament()
        elif choice == "4":
            self.reports_menu()
        elif choice == "5":
            self.update_player_elo()
        elif choice == "q":
            quit()
        else:
            self.error_view.display_error(1)
            self.main_menu()

    def reports_menu(self):
        choice = self.menu_view.reports_menu()
        if choice == "1":
            self.players_report(self.players)
        elif choice == "2":
            self.players_report_by_tournament()
        elif choice == "3":
            self.tournaments_report()
        elif choice == "4":
            self.rounds_report()
        elif choice == "5":
            self.matches_report()
        elif choice == "r":
            self.main_menu()
        else:
            self.error_view.display_error(1)
            self.reports_menu()

    # REPORTS #

    def players_report(self, players):
        choice = self.menu_view.sorting_menu()
        if choice == "1":
            sorted_players = sorted(players, key=lambda x: x.last_name)
            items = [x.__repr__() for x in sorted_players]
            self.reports_view.players_report(items)
            self.players_report(players)
        elif choice == "2":
            sorted_players = sorted(players, key=lambda x: x.elo, reverse=True)
            items = [x.__repr__() for x in sorted_players]
            self.reports_view.players_report(items)
            self.players_report(players)
        elif choice == "r":
            self.reports_menu()
        else:
            self.error_view.display_error(1)
            self.players_report(players)

    def players_report_by_tournament(self):
        tournament = self.choose_tournament()
        self.players_report(tournament.players)

    def tournaments_report(self):
        items = [x.__repr__() for x in self.tournaments]
        self.reports_view.tournaments_report(items)
        self.reports_menu()

    def rounds_report(self):
        tournament = self.choose_tournament()
        items = [x.__repr__() for x in tournament.rounds]
        self.reports_view.rounds_report(items, tournament)
        self.reports_menu()

    def matches_report(self):
        tournament = self.choose_tournament()
        round = self.choose_round(tournament)
        items = [[match.id, match.player1.__str__(),
                  match.player1_color,
                  match.player1_score,
                  match.player1.elo, str(),
                  match.player2.__str__(),
                  match.player2_color,
                  match.player2_score,
                  match.player2.elo] for match in round.matches if match.is_complete]
        self.reports_view.matches_report(items, tournament, round)
        self.reports_menu()

    # SETUP #

    def create_player(self):
        data = self.view.create_player()
        player = Player(**data)
        self.db.append_player(player)
        self.players.append(player)
        self.main_menu()

    def create_tournament(self):
        data_tournament = self.view.create_tournament()
        players = []
        player_index = 1
        while len(players) < PLAYERS_RANGE:
            data = self.view.add_player(player_index, PLAYERS_RANGE)
            for player in self.players:
                if str(player.id) == data and player not in players:
                    players.append(player)
                    player_index += 1
                    self.view.player_added(player)
                    break
            else:
                self.error_view.display_error(0)

        data_tournament["players"] = players
        tournament = Tournament(**data_tournament)
        self.db.append_tournament(tournament)
        self.tournaments.append(tournament)
        while True:
            choice = self.menu_view.play_tournament_menu(tournament)
            if choice == "1":
                self.play_tournament(tournament)
                break
            elif choice == "r":
                self.main_menu()
                break
            else:
                self.error_view.display_error(1)

    def update_player_elo(self):
        player = self.choose_player()
        new_elo = self.view.update_player_elo()
        player.elo = int(new_elo)
        self.db.update_player_elo(player)
        self.main_menu()

    # TOURNAMENT #

    def load_tournament(self):
        tournament = self.choose_tournament()
        if not tournament.is_complete:
            self.play_tournament(tournament)
        else:
            self.error_view.display_error(4)
            self.main_menu()

    def play_tournament(self, tournament):
        self.load_tournament_players(tournament)
        if not tournament.is_started:
            tournament.start()
        self.view.play_tournament(tournament)
        for round in tournament.rounds:
            if not round.is_complete:
                print(tournament.serialized())
                if not round.is_started:
                    round.start()
                for match in round.matches:
                    if not match.is_complete:
                        choice_available = False
                        while not choice_available:
                            self.view.start_match(round.name, match)
                            result = self.menu_view.play_match_menu(match.player1, match.player2)
                            if result == str(1):
                                match.play(1, 0)
                                self.db.update_tournament_rounds(tournament)
                                choice_available = True
                            elif result == str(2):
                                match.play(0, 1)
                                self.db.update_tournament_rounds(tournament)
                                choice_available = True
                            elif result == str(3):
                                match.play(0.5, 0.5)
                                self.db.update_tournament_rounds(tournament)
                                choice_available = True
                            elif result == "r":
                                choice_available = True
                                self.main_menu()
                            else:
                                self.error_view.display_error(1)
                round.complete()
                self.db.update_tournament(tournament)
        tournament.complete()
        self.db.update_tournament(tournament)
        self.main_menu()

    # CHOOSE #

    def choose_tournament(self):
        while True:
            tournament_id = self.view.choose_tournament()
            for tournament in self.tournaments:
                if tournament_id == str(tournament.id):
                    return tournament
                    break
            else:
                self.error_view.display_error(2)
                self.main_menu()

    def choose_round(self, tournament):
        while True:
            round_id = self.view.choose_round()
            for round in tournament.rounds:
                if round_id == str(round.id):
                    return round
                    break
            else:
                self.error_view.display_error(1)
                self.reports_menu()

    def choose_player(self):
        while True:
            player_id = self.view.choose_player()
            for player in self.players:
                if player_id == str(player.id):
                    return player
                    break
            else:
                self.error_view.display_error(3)

    def run(self):
        self.view.display_banner()
        self.main_menu()


# LANCEMENT DU PROGRAMME #
controller = Controller()
controller.load_players()
controller.load_tournaments()
controller.run()
