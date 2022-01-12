from LGBotProject.Role import Role


class LoupGarou(Role):
    nom = "Loup garou"
    ordre = 2

    def __init__(self):
        super(self.ordre)

    def playTurn(self, joueurs):
        # demande du joueur à tuer
        cible = self.findJoueurById("", joueurs)
        cible.setIsAlive(False)
        return cible.getId
