# Recebendo quatro valores do usuário : 
numeros = (
    int(input("Digite um número : ")),
    int(input("Digite outro número : ")),
    int(input("Digite mais um número : ")),
    int(input("Digite o último número : "))
)

print("O número 9 apareceu {} vezes;".format(numeros.count(9)))

if 3 in numeros:
    print("O número 3 apareceu na {} posição;".format(numeros.index(3)))
else:
    print("O número 3 não foi digitado!")

print("Os valores pares digitados são : ", end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end='')