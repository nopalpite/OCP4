from controllers.controller import Controller
from models.tournament import Tournament
from controllers.database import DatabaseController


PLAYERS_RANGE = 8


class TournamentController(Controller):

    def __init__(self):
        super().__init__()
        self.db_controller = DatabaseController()

    def create_tournament(self):
        data_tournament = self.view.create_tournament()
        players = []
        player_index = 1
        while len(players) < PLAYERS_RANGE:
            data = self.view.add_player(player_index, PLAYERS_RANGE)
            for player in self.players_list:
                if str(player.id) == data and player not in players:
                    players.append(player)
                    player_index += 1
                    self.view.player_added(player)
                    break
            else:
                self.error_view.display_error(0)
        data_tournament["players"] = players
        tournament = Tournament(**data_tournament)
        for player in tournament.players:
            player.score = 0
            player.have_played_with = []
        self.db.append_tournament(tournament)
        self.tournaments_list.append(tournament)
        while True:
            choice = self.menu_view.play_tournament_menu(tournament)
            if choice == "1":
                self.play_tournament(tournament)
                break
            elif choice == "r":
                return
            else:
                self.error_view.display_error(1)

    def load_tournament(self, tournament):
        if not tournament.is_complete:
            self.play_tournament(tournament)
        else:
            self.error_view.display_error(4)
            return

    def play_tournament(self, tournament):
        self.db_controller.load_tournament_players(tournament)
        if not tournament.is_started:
            tournament.start()
            self.db.update_tournament(tournament)
        self.view.play_tournament(tournament)
        for round in tournament.rounds:
            if not round.is_complete:
                if not round.is_started:
                    round.start()
                    self.db.update_tournament_rounds(tournament)
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
                                return
                            else:
                                self.error_view.display_error(1)
                round.complete()
                self.db.update_tournament(tournament)
        tournament.complete()
        self.db.update_tournament(tournament)
        return
