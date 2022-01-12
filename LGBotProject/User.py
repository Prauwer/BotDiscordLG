from LGBotProject.Role import Role


class User:
    isAlive = True
    lié = None

    def __init__(self, id):
        self.id = id
        self.role = Role()

    def getRole(self):
        return self.role

    def getVie(self):
        return self.vie

    def setVie(self, alive):
        self.isAlive = alive

    def getId(self):
        return self.id

    def setLié(self, user):
        self.lié = user
        user.setLié(self)

    def getLié(self):
        return self.lié
