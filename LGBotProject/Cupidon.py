from LGBotProject.Role import Role


class Cupidon(Role):
    nom = "Cupidon"
    ordre = 1

    def __init__(self):
        super(self.ordre)

    def playTurn(self, joueurs):
        # demande 2 utilisateur
        cible1 = self.findJoueurById(joueurs)
        cible2 = self.findJoueurById(joueurs)
        cible1.setLié(cible2)
        return cible1.getId(), cible2.getId()
