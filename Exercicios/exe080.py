expression = str(input("Digite uma expressão utilizando parênteses : "))

if expression.count("(") == expression.count(")"):
    print("Sua expressão está correta!")
else:
    print("Sua expressão está incorreta!")