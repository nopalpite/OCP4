from tinydb import TinyDB


class Database:

    def __init__(self):
        self.db = TinyDB('database.json')
        self.players_table = self.db.table('players')
        self.tournaments_table = self.db.table('tournaments')

    def append_player(self, player):
        player.id = self.players_table.insert(player.__dict__)
        self.players_table.update({'id': player.id}, doc_ids=[player.id])

    def append_tournament(self, tournament):
        tournament.id = self.tournaments_table.insert(tournament.serialized())
        self.tournaments_table.update({'id': tournament.id}, doc_ids=[tournament.id])

    def update_player_elo(self, player):
        self.players_table.update({'elo': player.elo}, doc_ids=[player.id])

    def update_tournament(self, tournament):
        for key, value in tournament.serialized().items():
            self.tournaments_table.update({key: value}, doc_ids=[tournament.id])

    def update_tournament_rounds(self, tournament):
        self.tournaments_table.update({'players': tournament.serialized()["players"]}, doc_ids=[tournament.id])
        self.tournaments_table.update({'rounds': tournament.serialized()["rounds"]}, doc_ids=[tournament.id])
