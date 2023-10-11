#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre : 

#1. Qual é o total gasto na compra;
#2. Quantos produtos custam mais de R$1000,00;
#3. Qual é o nome do produto mais barato;

from math import inf

preco = gasto = alto = 0
nome_barato = " "
barato = float(inf)

while True:
    nome = str(input("Digite o nome do produto : ")).strip().capitalize()
    preco = float(input("Digite o valor do produto : R$"))
    gasto += preco
    
    if preco > 1000.00:
        alto += 1
    if preco < barato:
        barato = preco
        nome_barato = nome
        
    resposta = str(input("Deseja continuar ? [S/N]\n>>> ")).strip().upper()[0:1]
    if resposta == "S":
        continue
    elif resposta == "N":
        print("Saindo...")
        break
    else:
        while True:
            resposta = str(input("Deseja continuar ? [S/N]\n>>> ")).strip().upper()[0:1]
            if resposta in "SN":
                break
    
print(f"Total de gasto : R${gasto}")
print(f"Total de produtos com valor maior que R$1000.00 : {alto}")
print(f"Nome do produto com menor preço : {nome_barato} | Valor do produto : R${barato}")