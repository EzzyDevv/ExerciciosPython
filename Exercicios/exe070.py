#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS : Considere que o caixa possuí cédulas de R$50,00, R$20,00, R$10,00 e R$1.

tot_50 = tot_20 = tot_10 = tot_1 = 0

print("=-"* 10)
print("| BANCO DO NUBANK | ")
print("=-"* 10)

while True:
    value = float(input("Qual o valor que deseja sacar ? R$"))
    
    if value.is_integer():
        break
    else:
        print("Digite novamente...")

print("Cédulas disponivéis : ( R$50,00 | R$20,00 | R$10,00 | R$1,00 )")
while True:
    print("Valor atual : R${:.2f}".format(value))
    cedulas = int(input("Digite qual cédula deseja : R$"))
     
    if cedulas == 50:
        tot_50 += quantidade

    if cedulas == 20:
        tot_20 += quantidade

    if cedulas == 10:
        tot_10 += quantidade

    if cedulas == 1:
        tot_1 += quantidade
        
    quantidade = int(input(f"Quantidade de cédulas que deseja de R${cedulas},00 : "))
    total = cedulas * quantidade
    
    if total > value:
        print("Quantidade maior do que a quantia de saque, digite corretamente!")
    else:
        value -= total
        if value == 0:
            print("Saque realizado.\nSaindo...")
            break
        else:
            continue
print(f"Total de cédulas de R$50,00 : {tot_50}\nTotal de cédulas de R$20,00 : {tot_20}\nTotal de cédulas de R$10,00 : {tot_10}\nTotal de cédulas de R$1,00 : {tot_1}")