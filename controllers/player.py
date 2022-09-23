from controllers.controller import Controller
from models.player import Player


class PlayerController(Controller):

    def create_player(self):
        data = self.view.create_player()
        player = Player(**data)
        self.db.append_player(player)
        self.players_list.append(player)
        return

    def update_player_elo(self, player):
        new_elo = self.view.update_player_elo()
        player.elo = int(new_elo)
        self.db.update_player_elo(player)
        return
