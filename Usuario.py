
class Usuario :

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sessionStarted = False

    def __str__(self):
        return "Nombre de usuario : "+self.username

    def changePassword(self, newPassword):
        if len(newPassword) >= 4 :
            self.password = newPassword
            print ("Se ha cambiado el password")
        else :
            print ("Password invalido. Debe tener mas de 4 caracteres")

    def login(self, username, password):
        if username == self.username & password == self.password :
            print("Ha iniciado sesion")
            self.sessionStarted = True
        else :
            print("El username o el password son icorrectos")

    def logout(self):
        print("Se ha cerrado la sesion")
        self.sessionStarted = False

            