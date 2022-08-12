from views.menu import MenuView
from views.reports import ReportsView
from views.error import ErrorView
from views.view import View
from models.player import Player
from models.tournament import Tournament

ROUND_RANGE = 4
PLAYERS_RANGE = 8


class Controller:

    def __init__(self):
        self.view = View()
        self.menu_view = MenuView()
        self.reports_view = ReportsView()
        self.error_view = ErrorView()
        self.players = []
        self.tournaments = []

    ############################ MENUS ############################

    def main_menu(self):
        choice = self.menu_view.main_menu()
        if choice == "1":
            self.create_tournament()
        elif choice == "2":
            self.create_new_player()
        elif choice == "3":
            self.load_tournament()
        elif choice == "4":
            self.reports_menu()
        elif choice == "q":
            quit()
        else:
            self.error_view.display_error(1)
            self.main_menu()

    def reports_menu(self):
        # TODO
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

    ############################ REPORTS #####################

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
        #TODO afficher uniquement les rounds terminés
        tournament = self.choose_tournament()
        items = [x.__repr__() for x in tournament.rounds]
        self.reports_view.rounds_report(items)
        self.reports_menu()

    def matches_report(self):
        #TODO afficher uniquement les matchs terminés
        tournament = self.choose_tournament()
        round = self.choose_round(tournament)
        items = [[x.id, x.player1.__str__(), x.player1.score, x.player1.elo, str(),
                  x.player2.__str__(), x.player2.score, x.player2.elo] for x in round.matches]
        self.reports_view.matches_report(items)
        self.reports_menu()


    ############################# SETUP ##########################

    def create_new_player(self):
        # TODO controller si le joueur n'existe pas déjà
        # TODO gérer la création de l'ID du joueur
        data = self.view.create_new_player()
        player = Player(**data)
        self.players.append(player)
        self.main_menu()

    def create_tournament(self):
        # TODO controller si le joueur n'existe pas déjà
        # TODO gérer la création de l'ID du tournoi
        data_tournament = self.view.create_tournament()
        players = []
        player_id = 1
        while len(players) < PLAYERS_RANGE:
            data = self.view.add_player(player_id, PLAYERS_RANGE)
            for player in self.players:
                if str(player.id) == data and player not in players:
                    players.append(player)
                    player_id += 1
                    self.view.player_added(player)
                    break
            else:
                self.error_view.display_error(0)

        data_tournament["players"] = players
        tournament = Tournament(**data_tournament)
        tournament.create_rounds()
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

    ################ TOURNAMENT #####################

    def load_tournament(self):
        #TODO ne charger que les tournois non terminés
        tournament = self.choose_tournament()
        self.play_tournament(tournament)

    def play_tournament(self, tournament):
        self.view.start_tournament(tournament)
        for round in tournament.rounds:
            if not round.is_complete:
                round.start()
                # TODO Tester match_is_complete
                for match in round.matches:
                    if not match.is_complete:
                        choice_available = False
                        while not choice_available:
                            self.view.start_match(round.name, match)
                            result = self.menu_view.play_match_menu(match.player1, match.player2)
                            if result == str(1):
                                match.play(1, 0)
                                choice_available = True
                            elif result == str(2):
                                match.play(0, 1)
                                choice_available = True
                            elif result == str(3):
                                match.play(0.5, 0.5)
                                choice_available = True
                            elif result == "r":
                                choice_available = True
                                self.main_menu()
                            else:
                                self.error_view.display_error(1)

                round.complete()

    ##################### CHOOSE #######################

    def choose_tournament(self):
        while True:
            tournament_id = self.view.choose_tournament()
            for tournament in self.tournaments:
                if tournament_id == str(tournament.id):
                    return tournament
                    break
            else:
                self.error_view.display_error(2)

    def choose_round(self, tournament):
        while True:
            round_id= self.view.choose_round()
            for round in tournament.rounds:
                if round_id == str(round.id):
                    return round
                    break
            else:
                self.error_view.display_error(1)


    def run(self):
        self.view.display_banner()
        self.main_menu()

######################TESTING SETUP########################################




controller = Controller()
controller.players = [Player("michel", "gerard", "date_1", "male", 1945),
                      Player("sylvain", "hervé", "date_2", "male", 1945),
                      Player("stéphanie", "croison", "date_4", "female", 178),
                      Player("cindy", "tartuffe", "date_4", "female", 97450),
                      Player("basile", "mitchell", "date_5", "male", 1945),
                      Player("nicolas", "bourges", "date_6", "male", 1945),
                      Player("kevin", "bratin", "date_7", "male", 178),
                      Player("lisa", "tarpot", "date_8", "female", 97450)]
id = 1
for player in controller.players:
    player.id = id
    id += 1
list = []
for i in controller.players:
    list.append(i)

controller.tournaments = [Tournament("Super tournoi", "bordeaux", list, "bullet"),
                          Tournament("Mega tournoi", "paris", controller.players, "bullet")]
controller.tournaments[0].id = 1
controller.tournaments[1].id = 2
controller.tournaments[
    0].description = "jdflksdjflkdsjlfkjsdlkfjlsdkjflksdjflkjdsl\nfkjdslkjflskdjflkdsjflkjsdlfkjsdlkjfslkjflskjdlksjflksdjflskj"

current_tournament = controller.tournaments[0]
current_tournament.create_rounds()


################## Lancement du programme ##########################


controller.run()
