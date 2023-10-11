palavras = ('proparoxitona', 'dissilaba', 'tretaplegico', 'discriminacao', 'pneumoultramicroscopicosilicovulcanoconiotico')
lista = []

for palavra in palavras:
    for letra in palavra:
        if letra.lower() in "aeiou":
            lista.append(letra)
    print(f"Palavra : {palavra} | Vogais : {lista}")
    lista = []