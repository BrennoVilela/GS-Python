class Drone:
    def __init__(self, id, modelo, bateria):
        self.id = id
        self.modelo = modelo
        self.bateria = bateria

    def captar_imagem(self):
        # Simula a captação de imagem
        return ["imagem_com_plastico"]

    def obter_coordenadas(self):
        # Coordenadas fictícias
        return "37.7749,-122.4194"

    def __str__(self):
        return f"Drone ID: {self.id}, Modelo: {self.modelo}, Bateria: {self.bateria}%"
