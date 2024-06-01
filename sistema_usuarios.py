from usuario import Usuario

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, nome, email, senha):
        if email in self.usuarios:
            return False
        self.usuarios[email] = Usuario(nome, email, senha)
        return True

    def login_usuario(self, email, senha):
        usuario = self.usuarios.get(email)
        if usuario and usuario.senha == senha:
            return usuario
        return None
