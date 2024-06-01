import tkinter as tk
from tkinter import messagebox, simpledialog
from drone import Drone
from sistema_deteccao_plastico import SistemaDeteccaoPlastico
from sistema_usuarios import SistemaUsuarios
from sistema_doacoes import SistemaDoacoes

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SOS Oceanos")
        self.sistema_usuarios = SistemaUsuarios()
        self.sistema_deteccao = SistemaDeteccaoPlastico()
        self.sistema_doacoes = SistemaDoacoes()
        self.drone = Drone("d001", "BJK", 96.2)
        self.usuario_atual = None
        self.logged_in = False

        self.show_cadastro_login()

    def show_cadastro_login(self):
        self.clear_window()

        tk.Label(self.root, text="Digite qual opção deseja acessar:").pack(pady=10)
        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_usuario).pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login_usuario).pack(pady=5)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(pady=5)

    def cadastrar_usuario(self):
        nome = simpledialog.askstring("Cadastro", "Digite seu nome:")
        email = simpledialog.askstring("Cadastro", "Digite seu email:")
        senha = simpledialog.askstring("Cadastro", "Digite sua senha:")

        if self.sistema_usuarios.cadastrar_usuario(nome, email, senha):
            messagebox.showinfo("Cadastro", "Cadastro feito com sucesso!")
        else:
            messagebox.showerror("Erro", "Email já cadastrado!")

    def login_usuario(self):
        email = simpledialog.askstring("Login", "Digite seu email:")
        senha = simpledialog.askstring("Login", "Digite sua senha:")

        self.usuario_atual = self.sistema_usuarios.login_usuario(email, senha)
        if self.usuario_atual:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.logged_in = True
            self.show_main_menu()
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")

    def show_main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Bem-vindo ao SOS Oceanos").pack(pady=10)
        tk.Button(self.root, text="Relatório de Poluição por Drone", command=self.relatorio_poluicao_drone).pack(pady=5)
        tk.Button(self.root, text="Doar para ONGs", command=self.doar_para_ongs).pack(pady=5)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(pady=5)

    def relatorio_poluicao_drone(self):
        imagem = self.drone.captar_imagem()
        plastico_detectado = self.sistema_deteccao.detectar_plastico(imagem)

        if plastico_detectado:
            coordenadas = self.drone.obter_coordenadas()
            quantidade_plastico = self.sistema_deteccao.contar_plastico(imagem)
            self.sistema_deteccao.registrar_local_poluido(coordenadas, quantidade_plastico)

        relatorio = self.sistema_deteccao.gerar_relatorio_poluicao()
        messagebox.showinfo("Relatório de Poluição por Drone", relatorio)
        messagebox.showinfo("Informações do Drone", str(self.drone))

    def doar_para_ongs(self):
        def confirmar_doacao(ong):
            valor = simpledialog.askfloat("Doação", "Digite quanto deseja doar:")
            self.sistema_doacoes.registrar_doacao(ong, valor, self.usuario_atual.get_nome())
            messagebox.showinfo("Doação", f"Obrigado(a), {self.usuario_atual.get_nome()}.\nVocê doou R${valor:.2f} para {ong}!")

        janela_doacao = tk.Toplevel(self.root)
        janela_doacao.title("Doar para ONGs")
        tk.Label(janela_doacao, text="Escolha uma ONG para doar:").pack(pady=10)
        tk.Button(janela_doacao, text="CoralGuardians: Preservação de recifes de corais", command=lambda: confirmar_doacao("CoralGuardians")).pack(pady=5)
        tk.Button(janela_doacao, text="CleanWave: Limpeza de lixo plástico dos oceanos", command=lambda: confirmar_doacao("CleanWave")).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
