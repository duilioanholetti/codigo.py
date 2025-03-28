import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número entre 1 e 100!")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif
