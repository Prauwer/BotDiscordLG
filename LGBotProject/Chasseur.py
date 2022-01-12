from LGBotProject.Role import Role


class Chasseur(Role):
    nom = "Chasseur"
    ordre = 0

    def __init__(self):
        super(self.ordre)

    def playTurn(self, joueurs):
        # demande id
        cible = self.findJoueurById(joueurs)
        cible.setIsAlive(False)
        return cible.getId()
