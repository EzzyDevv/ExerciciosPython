#Importação de múdulos
from random import randint


# Variáveis necessárias
numero_computador = randint(0, 10)
chute = 0
total_chutes = 0

#Estrutura while
while True:
    chute = int(input("Tente acertar o número de 0 a 10 em que o computador pensou : "))
    total_chutes += 1
    if chute == numero_computador:
        print(f"Você acertou!\nO total de tentativas foi : {total_chutes}")
        break
    else:
        if chute < numero_computador:
            print("Mais... Tente novamente!")
        else:
            print("Menos... Tente novamente!")