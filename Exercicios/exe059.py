#Importação de módulos
from time import sleep
import subprocess

# Entrada de valores | Tipo : Inteiro
primary = int(input("Digite um número : "))
second = int(input("Digite outro número : "))

#Mostrando menu dentro de uma estrutura while
while True:
    sleep(5)
    subprocess.run('clear', shell=True)
    #Entrada de uma variável do tipo inteiro com escopo local & Verificação de condicional
    option = int(input(("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do Programa\n>>> ")))
    if option == 1:
        print("A soma entre os números digitados é : {}".format(primary + second))
    elif option == 2:
        print("A multiplicação entre os números digitados é : {}".format(primary * second))
    elif option == 3:
        print("O maior número digitado foi : {}".format(max(primary, second)))
    elif option == 4:
        primary = int(input("Digite um número : "))
        second = int(input("Digite outro número : "))
    elif option == 5:
        print("Finalizando...")
        break
    else:
        print("Digite um valor corretamente!")
print(primary, second)