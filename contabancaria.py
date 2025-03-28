class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Criando uma conta
conta = ContaBancaria("João Silva", 500)

# Operações bancárias
conta.consultar_saldo()
conta.depositar(300)
conta.sacar(
