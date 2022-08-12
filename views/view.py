

BANNER = """ __        ___  __   __     ___  __        __                   ___      ___
/  ` |__| |__  /__` /__`     |  /  \ |  | |__) |\ |  /\   |\/| |__  |\ |  |
\__, |  | |___ .__/ .__/     |  \__/ \__/ |  \ | \| /~~\  |  | |___ | \|  |
                                                                             """
class View:

    def display_banner(self):
        print(BANNER)

    def create_tournament(self):
        print()
        print("------Nouveau Tournoi------")
        name = input("entrez le nom du tournoi: ")
        place = input("entrez le lieux du tournoi: ")
        time_control = input("entrez le contrôle du temps (Bullet/Blitz/Coup rapide): ")
        print()
        return {"name": name.capitalize(), "place": place.capitalize(), "time_control": time_control.capitalize()}

    def create_new_player(self):
        print("------Nouveau Joueur------")
        first_name = input("entrez le prénom du joueur: ")
        last_name = input("entrez le nom de famille du joueur: ")
        birth_date = input("entrez la date de naissance du joueur(jj/mm/aa): ")
        gender = input("entrez le genre du joueur(H/F): ")
        elo = input("entrez le classement ELO du joueur: ")
        print()
        return {"first_name": first_name.capitalize(), "last_name": last_name.capitalize(), "birth_date": birth_date, "gender": gender.upper(),
                "elo": int(elo)}

    def add_player(self, player_id, players_range):
        print(f"------Inscription joueur {player_id}/{players_range}")
        id = input(f"entrez l'ID du joueur {player_id}: ")
        return str(id)

    def player_added(self, player):
        print(f"inscription de {player} au tournoi")
        print()

    def start_tournament(self, tournament):
        print(tournament)
        print()

    def choose_tournament(self):
        choice = input("Entrez l'ID du tournoi: ")
        return choice

    def choose_round(self):
        choice = input("Entrez le numéro du tour(1-4): ")
        return choice

    def start_match(self, round, match):
        print(f"++++++{round}++++++")
        print(f"------{match.__str__()}------")
        print()
