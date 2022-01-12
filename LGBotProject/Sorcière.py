from LGBotProject.Role import Role


class Sorcière(Role):
    nom = "Sorcière"
    ordre = 3

    def __init__(self):
        super(self.ordre)

    def playTurn(self, joueurs):
        # demande soin/tuer
        sort = True
        # demande id
        cible = self.findJoueurById("", joueurs)
        cible.setIsAlive(sort)
        return cible.getId, sort
