numbers = (
    'zero',
    'um',
    'dois',
    'tres',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze'
    'quatorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

print("Digite 999 para encerrar o programa!")
while True:
    x = int(input("Digite um número de 0 até 20 : "))
    if x == 999:
        print("Saindo...")
        break
    while x < 0 or x > 20:
        x = int(input("Digite um número de 0 até 20 : "))
    print(f"Número digitado : {x} | Número digitado por extenso : {numbers[x]}")