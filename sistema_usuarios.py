class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, nome, email, senha):
        if email in self.usuarios:
            return False
        self.usuarios[email] = {"nome": nome, "senha": senha}
        return True

    def login_usuario(self, email, senha):
        if email in self.usuarios and self.usuarios[email]["senha"] == senha:
            return self.usuarios[email]
        return None
