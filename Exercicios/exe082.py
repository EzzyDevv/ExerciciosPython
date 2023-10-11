lista_geral = [[], [], []]

while True:
    number = int(input("Digite um número : "))
    lista_geral[0].append(number)
    if number % 2 == 0:
        lista_geral[1].append(number)
    else:
        lista_geral[2].append(number)
    resposta = str(input("Deseja continuar ? [S/N]\n>>> ")).strip().lower()
    if resposta in 'n':
        break
print(f"Os números digitados foram : {lista_geral[0]}")
print(f"Os números pares digitados foram : {lista_geral[1]}")
print(f"Os números ímpares digitados foram : {lista_geral[2]}")