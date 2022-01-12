class Role:

    def __init__(self, ordre):
        self.ordre = ordre

    def playTurn(self):
        return

    def getOrdre(self):
        return self.ordre

    def findJoueurById(self, id, joueurs):
        for j in joueurs:
            if id == j.getId():
                return j
