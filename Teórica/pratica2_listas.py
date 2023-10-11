valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input("Digite um valor : ")))

for i, v in enumerate(valores):
    print(f"Na posição {i} encontrei o valor {v}")
print("Cheguei ao final da lista!")