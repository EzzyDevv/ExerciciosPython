soma = total_digitados = 0

print("Para sair do programa, digite ( 999 )!")
while True:
    number = int(input("Digite um número : "))
    
    if number == 999:
        print("Saindo...")
        break
    else:
        soma += number
        total_digitados += 1
print(f"A soma dos {total_digitados} é {soma}.")