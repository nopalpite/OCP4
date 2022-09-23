from controllers.controller import Controller


class ReportsController(Controller):

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
            return
        else:
            self.error_view.display_error(1)
            self.players_report(players)

    def players_report_by_tournament(self, tournament):
        self.players_report(tournament.players)

    def tournaments_report(self):
        items = [x.__repr__() for x in self.tournaments_list]
        self.reports_view.tournaments_report(items)

    def rounds_report(self, tournament):
        items = [x.__repr__() for x in tournament.rounds]
        self.reports_view.rounds_report(items, tournament)

    def matches_report(self, tournament, round):
        items = [[match.id, match.player1.__str__(),
                  match.player1_color,
                  match.player1_score,
                  match.player1.elo, str(),
                  match.player2.__str__(),
                  match.player2_color,
                  match.player2_score,
                  match.player2.elo] for match in round.matches if match.is_complete]
        self.reports_view.matches_report(items, tournament, round)
