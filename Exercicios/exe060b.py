number = int(input("Digite o número para calcular o fatorial : "))
c = number
f = 1

print("{}! =".format(number), end=" ")
while c > 0:
    print("{}".format(c), end=" ")
    print("x" if c > 1 else "=", end=" ")
    f *= c
    c -= 1
print(f)