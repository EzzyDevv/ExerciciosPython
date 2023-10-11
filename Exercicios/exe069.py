idade = 0
sexo = ' '
maior_18 = mulheres_20 = homens_cadastrados = 0

print("-"*23)
print("| CADASTRO DE PESSOAS | ")
print("-"*23)

while True:
    idade = int(input("Digite sua idade : "))
    sexo = str(input("Digite seu sexo : [M/F]")).upper().strip()[0:1]
    
    if idade > 18:
        maior_18 += 1
    if sexo in 'Mm':
        homens_cadastrados += 1
    if idade > 20 and sexo in 'Ff':
        mulheres_20 += 1

    answer = str(input("Deseja continuar ? [S/N]")).strip()[0:1]
    if answer in 'Ss':
        continue
    else:
        print("Saindo...")
        break

print("Total de pessoas maiores de 18 anos : {}".format(maior_18))
print("Total de homens cadastrados : {}".format(homens_cadastrados))
print("Total de mulheres com mais de 20 anos cadastrados : {}".format(mulheres_20))