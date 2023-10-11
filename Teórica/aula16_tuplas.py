# Observações : 

# - Não é possível alterar um valor de uma tupla, anão ser diretamente;
# Uma tupla é igual uma lista, a única diferença é que uma tupla é imutável;

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudin')
print(lanche[1:])
print(len(lanche))

c = 0
while c <= len(lanche) - 1:
    print(lanche[c])
    c += 1
    
for x in lanche:
    print(x)