lista = []

for c in range(0, 5):
    n = int(input("Digite um valor : "))
    if c == 0 or n > lista[len(lista) - 1]:
        lista.append(n)
        print("Adicionado ao final da lista.")
    else:
        contador = 0
        while contador < len(lista):
            if n <= lista[contador]:
                lista.insert(contador, n)
                print(f"Adicionado na posição {contador} da lista.")
                break
            contador += 1
print(f"Os valores digitados em ordem foram {lista}")