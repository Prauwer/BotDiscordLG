from LGBotProject.Role import Role


class User:
    vie = True

    def __init__(self, nom):
        self.nom = nom
        self.role = Role()

    def getRole(self):
        return self.role

    def getVie(self):
        return self.vie

    def setVie(self, vie):
        self.vie = vie
