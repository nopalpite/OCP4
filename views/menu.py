class MenuView:

    def display_menu(self, header, choices, main: bool):
        if header:
            if main:
                print(f"###### {header.upper()} ######")
                print()
            else:
                print(f"------{header}------")
                print()

        index = 1
        for choice in choices:
            print(f"[{index}] {choice.capitalize()}")
            index += 1
        print()
        if main:
            print("[q] Quitter")
        else:
            print("[r] Retour")
        choice = input("Entrez votre choix: ")
        print()
        return choice


    def main_menu(self):
        header = "menu principal"
        choices = ["créer un tournoi",
                   "ajouter des joueurs à la base de donnée",
                   "charger un tournoi",
                   "afficher un rapport"]
        return self.display_menu(header, choices, True)

    def reports_menu(self):
        header = "menu des rapports"
        choices = ["liste des joueurs",
                   "liste des joueurs par tournoi",
                   "liste des tournois",
                   "liste des tours par tournoi",
                   "liste des matchs par tournoi"]
        return self.display_menu(header, choices, False)

    def sorting_menu(self):
        choices = ["par ordre alphabétique",
                   "par classement"]
        return self.display_menu(False, choices, False)


    def play_tournament_menu(self, tournament):
        print(f"------{tournament}------")
        choices = ["lancer le tournoi"]
        return self.display_menu(False, choices, False)


    def play_match_menu(self,player1, player2):
        choices = [f"{player1} gagne",
                   f"{player2} gagne",
                   "égalité"]
        return self.display_menu(False, choices, False)
