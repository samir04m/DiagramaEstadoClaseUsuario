from usuario import Usuario

user = Usuario("samir04m", "1234")

user.login("samir04m", "123")
user.login("samir04m", "1234")

user.changePassword("432")
user.changePassword("4321")

user.logout()