class ErrorView:

    def display_error(self, error):
        if error == 0:
            print("ID joueur invalide, ou joueur déjà inscrit au tournoi \n")
        elif error == 1:
            print("Veuillez faire un choix valide \n")
        elif error == 2:
            print("ID tournoi invalide\n")
        else:
            print("Erreur inconnue\n")