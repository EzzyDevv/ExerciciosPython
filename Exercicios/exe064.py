lista = []
total_digitados = soma = 0

while True:
    number = int(input("Digite um número : "))
    lista.append(number)
    total_digitados += 1
    soma += number
    
    resposta = str(input("Deseja digitar mais um número : [S/N]")).upper().strip()[0]
    if resposta in 'Ss':
        continue
    else:
        break
print("Total de Números Digitados : {}".format(total_digitados))
print("Média dos valores digitados : {:.1f}".format(soma / total_digitados))
print("Maior número digitado : {}\nMenor número digitado : {}".format(max(lista), min(lista)))