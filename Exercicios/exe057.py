# Entrada de Dados | Looping While

print("Observação : Será aceito somente [M/F], qualquer outro caractere digitado será visto como incorreto!")
while True:
    sexo = str(input("Digite seu sexo : [M/F] >>> ")).upper().strip()[0]
    if sexo == 'M':
        print("Sexo cadastrado com sucesso!")
        break
    if sexo == 'F':
        print("Sexo cadastrado com sucesso!")
        break
    else:
        print("Incorreto, digite novamente...")