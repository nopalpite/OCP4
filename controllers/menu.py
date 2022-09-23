from controllers.controller import Controller
from controllers.player import PlayerController
from controllers.reports import ReportsController
from controllers.tournament import TournamentController
from controllers.database import DatabaseController


class MenuController(Controller):

    def __init__(self):
        super().__init__()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.report_controller = ReportsController()
        self.db_controller = DatabaseController()

    # MENUS #

    def main_menu(self):
        choice = self.menu_view.main_menu()
        if choice == "1":
            self.tournament_controller.create_tournament()
            self.main_menu()
        elif choice == "2":
            self.player_controller.create_player()
            self.main_menu()
        elif choice == "3":
            tournament = self.choose_tournament()
            self.tournament_controller.load_tournament(tournament)
            self.main_menu()
        elif choice == "4":
            self.reports_menu()
        elif choice == "5":
            player = self.choose_player()
            self.player_controller.update_player_elo(player)
            self.main_menu()
        elif choice == "q":
            quit()
        else:
            self.error_view.display_error(1)
            self.main_menu()

    def reports_menu(self):
        choice = self.menu_view.reports_menu()
        if choice == "1":
            self.report_controller.players_report(self.players_list)
            self.reports_menu()
        elif choice == "2":
            tournament = self.choose_tournament()
            self.report_controller.players_report_by_tournament(tournament)
            self.reports_menu()
        elif choice == "3":
            self.report_controller.tournaments_report()
            self.reports_menu()
        elif choice == "4":
            tournament = self.choose_tournament()
            self.report_controller.rounds_report(tournament)
            self.reports_menu()
        elif choice == "5":
            tournament = self.choose_tournament()
            round = self.choose_round(tournament)
            self.report_controller.matches_report(tournament, round)
            self.reports_menu()
        elif choice == "r":
            self.main_menu()
        else:
            self.error_view.display_error(1)
            self.reports_menu()

    def choose_tournament(self):
        while True:
            tournament_id = self.view.choose_tournament()
            for tournament in self.tournaments_list:
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
            for player in self.players_list:
                if player_id == str(player.id):
                    return player
                    break
            else:
                self.error_view.display_error(3)

    def run(self):
        self.db_controller.load_db()
        self.main_menu()
