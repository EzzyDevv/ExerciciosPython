string = "O brasil é o país do futebol"

# Utilizando método ' split() ' para transformar uma string em uma lista, passando uma determinada separação : 

lista_1 = string.split(' ')
print(lista_1)

for value in lista_1:
    print(value.strip().capitalize())
