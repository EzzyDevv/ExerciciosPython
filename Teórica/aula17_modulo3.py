
#Adicionando valores a uma lista
lista = ['hamburguer', 'suco', 'pizza', 'picolé']
print(lista)

# Adicionando valores em um índice desejado da lista.
lista.insert(0, 'abacaxi')
print(lista)

# Adicionado valores ao final da lista.
lista.append('melancia')
print(lista)

# Eliminando valores de uma lista de um determinado índice.
del lista[1]
print(lista)

# Eliminando o valor final de uma lista, porém é possível também remover por índice
lista.pop(3)
print(lista)

# Eliminando um valor de uma lista, especificando o valor, não o índice;
lista.remove('suco')
print(lista)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-

# Criação de lista usando o range()
numbers = list(range(4, 11))
print(numbers)

#Colocando uma lista em ordem usando o método sort()
numbers_2 = [1, 6, 3, 27, 7, 54, 876, 4, 76, 5]
numbers_2.sort()
print(numbers_2)

# Quantidade de valores em uma lista usando o método len()
print(len(numbers_2))