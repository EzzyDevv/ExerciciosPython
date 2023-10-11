lista = []

while True:
    number = int(input("Digite um número : "))
    if number in lista:
        print("Número duplicado, não será adicionado...")
        continue
    else:
        print("Adicionado na lista...")
        lista.append(number)
        
    resposta = str(input("Deseja continuar ? [s/n]\n>>> ")).strip().lower() == 's'
        
    if resposta:
        continue
    else:
        print("Saindo...")
        break
print(sorted(lista))