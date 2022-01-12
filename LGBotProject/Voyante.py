from LGBotProject.Role import Role


class Voyante(Role):
    nom = "Voyante"
    ordre = 4

    def __init__(self):
        super(self.ordre)

    def playTurn(self, joueurs):
        # demande cible
        cible = self.findJoueurById(joueurs)
        affiche = cible.getRole()
        # afficher affiche
