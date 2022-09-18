import pyfiglet


class View:

    def display_banner(self):
        ascii_banner = pyfiglet.figlet_format("CHESS TOURNAMENT")
        print(ascii_banner)

    def create_tournament(self):
        print()
        print("------Nouveau Tournoi------")
        name = input("entrez le nom du tournoi: ")
        place = input("entrez le lieux du tournoi: ")
        time_control = input("entrez le contrôle du temps (Bullet/Blitz/Coup rapide): ")
        description = input("entrez la description du tournoi: ")
        print()
        return {"name": name.capitalize(),
                "place": place.capitalize(),
                "time_control": time_control.capitalize(),
                "description": description
                }

    def create_player(self):
        print("------Nouveau Joueur------")
        first_name = input("entrez le prénom du joueur: ")
        last_name = input("entrez le nom de famille du joueur: ")
        birth_date = input("entrez la date de naissance du joueur(jj/mm/aaaa): ")
        gender = input("entrez le genre du joueur(H/F): ")
        elo = input("entrez le classement ELO du joueur: ")
        print()
        return {"first_name": first_name.capitalize(),
                "last_name": last_name.capitalize(),
                "birth_date": birth_date,
                "gender": gender.upper(),
                "elo": int(elo)
                }

    def choose_player(self):
        id = input("entrez l'ID du joueur: ")
        return id

    def update_player_elo(self):
        new_elo = input("entrez le nouveau elo du joueur: ")
        return new_elo

    def add_player(self, player_index, players_range):
        print(f"------Inscription joueur {player_index}/{players_range}")
        id = input(f"entrez l'ID du joueur {player_index}: ")
        return str(id)

    def player_added(self, player):
        print(f"inscription de {player} au tournoi")
        print()

    def play_tournament(self, tournament):
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
