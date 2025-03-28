class Jogador:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

    def executar_funcao(self):
        if self.funcao == "Atacante":
            return f"{self.nome} está atacando!"
        elif self.funcao == "Defensor":
            return f"{self.nome} está defendendo!"
        elif self.funcao == "Meio-campo":
            return f"{self.nome} está controlando o meio de campo!"
        elif self.funcao == "Goleiro":
            return f"{self.nome} está defendendo no gol!"
        elif self.funcao == "Lateral":
            return f"{self.nome} está avançando pela lateral!"
        else:
            return f"{self.nome} tem uma função desconhecida!"

def criar_time():
    jogadores = []
    for i in range(5):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        funcao = input(f"Digite a função do jogador {i + 1} (Atacante, Defensor, Meio-campo, Goleiro, Lateral): ")
        jogador = Jogador(nome, funcao)
        jogadores.append(jogador)
    return jogadores

def exibir_funcoes(jogadores):
    print("\nFunções dos jogadores no time:")
    for jogador in jogadores:
        print(jogador.executar_funcao())

# Criação do time
time = criar_time()

# Exibição das funções dos jogadores
exibir_funcoes(time)
