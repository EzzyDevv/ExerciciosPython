from random import randint
total_ganhos = 0
usuario = ' '

while True:
    aleatorio = randint(0, 10)
    usuario = str(input("PAR ou IMPAR ? [P/I]\n>>> ")).upper().strip()[0:1]
    
    while True:
        if usuario not in 'PI':
            usuario = str(input("PAR ou IMPAR ? [P/I]\n>>> "))
        else:
            break
    
    numero_usuario = int(input("Digite um número : "))
    resultado = aleatorio + numero_usuario
    
    print(f"Você jogou {numero_usuario} e o computador jogou {aleatorio}, o total é {resultado}!")
    print("DEU PAR" if resultado % 2 == 0 else "DEU ÍMPAR")
    
    if usuario in "P" and resultado % 2 == 0:
        total_ganhos += 1
        print("Você ganhou!")
    elif usuario in "I" and resultado % 2 == 1:
        total_ganhos += 1
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        break
    print("Vamos jogar mais uma vez...")
print(f"Total de ganhos consecutivos : {total_ganhos}")