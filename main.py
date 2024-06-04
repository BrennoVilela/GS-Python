import tkinter as tk
from tkinter import simpledialog, messagebox
from drone import Drone
from sistema_deteccao import SistemaDeteccaoPlastico
from sistema_usuarios import SistemaUsuarios
from sistema_doacoes import SistemaDoacoes

def main():
    # Instancia do drone
    drone = Drone("d001", "BJK", 96.2)

    # Instancia do sistema de detecção de plástico
    sistema = SistemaDeteccaoPlastico()

    # Instancia do sistema de usuários
    sistema_usuarios = SistemaUsuarios()

    # Instancia do sistema de doações
    sistema_doacoes = SistemaDoacoes()

    usuario_atual = None

    # Área de Cadastro e Login
    logged_in = False
    while not logged_in:
        opcao_cadastro = simpledialog.askinteger("Opção", "Digite qual opção deseja acessar:\n1 - Cadastrar\n2 - Login\n3 - Sair")

        if opcao_cadastro == 1:
            nome = simpledialog.askstring("Cadastro", "Digite seu nome:")
            email = simpledialog.askstring("Cadastro", "Digite seu email:")
            senha = simpledialog.askstring("Cadastro", "Digite sua senha:", show='*')

            if nome and email and senha:
                if sistema_usuarios.cadastrar_usuario(nome, email, senha):
                    messagebox.showinfo("Cadastro", "Cadastro feito com sucesso!")
                else:
                    messagebox.showinfo("Cadastro", "Email já cadastrado!")
            else:
                messagebox.showwarning("Cadastro", "Por favor, preencha todos os campos.")

        elif opcao_cadastro == 2:
            email = simpledialog.askstring("Login", "Digite seu email:")
            senha = simpledialog.askstring("Login", "Digite sua senha:", show='*')

            usuario_atual = sistema_usuarios.login_usuario(email, senha)

            if usuario_atual:
                messagebox.showinfo("Login", "Login bem-sucedido!")
                logged_in = True
            else:
                messagebox.showwarning("Login", "Email ou senha incorretos!")

        elif opcao_cadastro == 3:
            messagebox.showinfo("SOS Oceanos", "Obrigado por utilizar o SOS Oceanos")
            return

        else:
            messagebox.showwarning("Opção Inválida", "Opção inválida! Por favor, escolha uma opção válida.")

    # Apresentação do site
    messagebox.showinfo("SOS Oceanos", "Bem vindo ao SOS Oceanos")

    # Área do Menu Principal
    opcao = None
    while opcao != 3:
        opcao = simpledialog.askinteger("Opção", "Digite qual opção deseja acessar:\n1 - Relatório de Poluição por Drone\n2 - Doar para ONGS\n3 - Sair")

        if opcao == 1:
            # Processar imagem do drone
            imagem = drone.captar_imagem()
            plastico_detectado = sistema.detectar_plastico(imagem)

            if plastico_detectado:
                coordenadas = drone.obter_coordenadas()
                quantidade_plastico = sistema.contar_plastico(imagem)
                sistema.registrar_local_poluido(coordenadas, quantidade_plastico)

            # Gerar relatório de poluição
            relatorio = sistema.gerar_relatorio_poluicao()
            messagebox.showinfo("Relatório de Poluição", relatorio)

            # Exibir informações do drone
            messagebox.showinfo("Drone", str(drone))

        elif opcao == 2:
            opcao_ong = None
            while opcao_ong != 3:
                opcao_ong = simpledialog.askinteger("ONG", "Digite a opção que deseja acessar:\n1 - CoralGuardians: Preservação de recifes de corais\n2 - CleanWave: Limpeza de lixo plástico dos oceanos\n3 - Voltar")

                if opcao_ong == 1:
                    valor = simpledialog.askfloat("Doação", "Digite quanto deseja doar:")
                    if valor:
                        sistema_doacoes.registrar_doacao("CoralGuardians", valor, usuario_atual["nome"])
                        messagebox.showinfo("Doação", f"Obrigado(a), {usuario_atual['nome']}. Você doou R${valor} para a CoralGuardians!")

                elif opcao_ong == 2:
                    valor = simpledialog.askfloat("Doação", "Digite quanto deseja doar:")
                    if valor:
                        sistema_doacoes.registrar_doacao("CleanWave", valor, usuario_atual["nome"])
                        messagebox.showinfo("Doação", f"Obrigado(a), {usuario_atual['nome']}. Você doou R${valor} para a CleanWave!")

                elif opcao_ong == 3:
                    break

                else:
                    messagebox.showwarning("Opção Inválida", "Opção inválida! Por favor, escolha uma opção válida.")

        elif opcao == 3:
            messagebox.showinfo("SOS Oceanos", "Obrigado por utilizar o SOS Oceanos")

        else:
            messagebox.showwarning("Opção Inválida", "Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
