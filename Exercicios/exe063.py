tot = som = 0
print("Digite quantos números desejar, caso não queira mas, digite 999")
while True:
    number = int(input("Digite um número : "))
    if number == 999:
        print("Saindo...")
        break
    else:
        tot += 1
        som += number
print(f"Total de Números Digitados : {tot}\nSoma de todos os valores digitados : {som}")