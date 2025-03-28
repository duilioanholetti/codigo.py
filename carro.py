class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._velocidade = 0

    def acelerar(self, incremento):
        self._velocidade += incremento
        print(f"{self.modelo} acelerou para {self._velocidade} Km/h")

    def mover(self):
        pass

    def get_velocidade(self):
        return self._velocidade


class Carro(Veiculo):
    def mover(self):
        print(f"O carro {self.modelo} está dirigindo na estrada")



c1 = Carro("Toyota", "Corolla", "2022")


c1.mover()
c1.acelerar(50)

print("Velocidade atual:", c1.get_velocidade())
