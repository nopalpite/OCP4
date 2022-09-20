class ErrorView:
    """ErrorView class"""

    def display_error(self, error):
        if error == 0:
            print("ID joueur invalide, ou joueur déjà inscrit au tournoi \n")
        elif error == 1:
            print("Veuillez faire un choix valide \n")
        elif error == 2:
            print("ID tournoi invalide\n")
        elif error == 3:
            print("ID joueur invalide\n")
        elif error == 4:
            print("Ce tournoi est déjà terminé\n")
        else:
            print("Erreur inconnue\n")
