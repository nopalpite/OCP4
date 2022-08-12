from tabulate import tabulate


class ReportsView:

    def report(self, rows, items):
        table = [rows]
        for item in items:
            table.append(item)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        print()

    def players_report(self, players_items):
        rows = ['ID',
                'Nom',
                'Prénom',
                'Genre',
                'Date de naissance',
                'Elo']
        self.report(rows, players_items)

    def tournaments_report(self, tournaments_items):
        rows = ['ID',
                'Nom ',
                'Lieu',
                'Date de début',
                'Date de fin',
                'Description']
        self.report(rows, tournaments_items)

    def rounds_report(self, rounds_items):
        rows = ['Round',
                'Date de début',
                'Date de fin',
                'Matchs']
        self.report(rows, rounds_items)

    def matches_report(self, matches_items):
        rows = ['Match',
                'Joueur 1',
                'Score ',
                'Elo',
                'VS',
                'Joueur 2',
                'Score',
                'Elo']
        self.report(rows, matches_items)
