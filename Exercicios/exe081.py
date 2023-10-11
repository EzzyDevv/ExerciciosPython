lista = []

while True:
    lista.append(int(input("Digite um número : ")))
    resposta = str(input("Deseja continuar ? [s/n]\n>>> ")).strip().lower()
    if 'n' in resposta:
        print("Stop looping!")
        break 
 
print("O total de números digitados foram : {}".format(len(lista)))
lista.sort(reverse=True)
print("Números digitados decrescente : {}".format(lista))
if 5 in lista:
    print("O número 5 foi digitado!!!")
else:
    print("O número 5 não foi digitado!")