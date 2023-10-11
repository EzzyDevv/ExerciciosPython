term_primary = int(input("Digite o 1° Termo : "))
difference = int(input("Digite a razão : "))
tot = 10
c = 1
standard_value = 10

while True:
    while c <= standard_value:
        print("{}° Termo : {}".format(c, term_primary))
        term_primary += difference
    
        c += 1
    answer = int(input("Digite até qual termo deseja ver mais ou digite 0 para sair : "))
    if answer == 0:
        print("Saindo...")
        break
    else:
        tot += answer
        c = 1
        standard_value = answer
print("Progressão finalizada, o total de termos mostrado é : {}".format(tot))