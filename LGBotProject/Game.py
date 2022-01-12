from LGBotProject.User import User


class Game:
    tour = 0
    nuit = True
    game = True
    joueurs = []

    def __init__(self, nbr_joueurs):
        if nbr_joueurs <= 8:
            self.initGame(nbr_joueurs)

    def initGame(self, nbr_joueurs):
        for i in range(nbr_joueurs):
            self.joueurs.append(User("name"))
        self.startGame()

    def startGame(self):
        while self.game:
            self.tour += 1
            if self.nuit:
                for j in self.joueurs:
                    if j.getRole().getOrdre() != 0:
                        j.playTurn()
            else:
                pass



