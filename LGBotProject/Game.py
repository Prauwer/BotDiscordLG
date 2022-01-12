from LGBotProject.LoupGarou import LoupGarou
from LGBotProject.User import User


class Game:
    tour = 0
    nuit = True
    game = True
    nbr_vil = 0
    nbr_loup = 0
    joueurs = []
    loupGarouHasPlayed = False

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
                self.loupGarouHasPlayed = False
                self.playNight()
            else:
                self.playDay()

            if self.endGame():
                self.game = False

    def endGame(self):
        return self.nbr_loup == 0 or self.nbr_loup >= self.nbr_vil

    def playNight(self):
        for j in self.joueurs:
            if j.getRole().getOrdre() != 0 and j.getIsAlive():
                if isinstance(j.getRole(), LoupGarou) and self.loupGarouHasPlayed:
                    self.loupGarouHasPlayed = True
                else:
                    j.playTurn()

    def playDay(self):
        vote = []
        for j in self.joueurs:
            if j.getIsAlive():
                # demande de vote
                for i in self.joueurs:
                    if i.getNom() == "":
                        vote.append(i)
        maxi = 0
        for j in self.joueurs:
            if vote.count(j) > maxi:
                maxi = vote.count(j)
                mort = j
        mort.setIsAlive(False)

    def findJoueurById(self, id):
        for j in self.joueurs:
            if id == j.getId():
                return j
