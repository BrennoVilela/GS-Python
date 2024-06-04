class Drone:
    def __init__(self, id, location, battery):
        self.id = id
        self.location = location
        self.battery = battery

    def captar_imagem(self):
        # Simulação de captura de imagem
        return ["image_data"]

    def obter_coordenadas(self):
        # Simulação de obtenção de coordenadas
        return "123.456, -789.012"

    def __str__(self):
        return f"Drone ID: {self.id}, Location: {self.location}, Battery: {self.battery}%"
