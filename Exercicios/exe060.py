#Entrada de dados
number = int(input("Digite um número que deseja ver o factorial : "))
#Criação da lista
lista = list(range(number, 0, -1))

#Mostrando o fatorial do valor recebido
print(' x '.join(str(i) for i in lista), end=" : ")

#Iteração sobre alista e descobrindo valor
fat = number
for i in lista[1::]:
    fat *= i
print(fat)