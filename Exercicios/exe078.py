numbers = []
maior = menor = 0

for i in range(0, 6):
    n = int(input("Digite um número : "))
    numbers.append(n)
    if i == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"O maior valor digitado foi : {maior} e esse valor se encontra na posição {numbers.index(maior)}")
print(f"O menor valor digitado foi : {menor} e esse valor se encontra na posição {numbers.index(menor)}")
