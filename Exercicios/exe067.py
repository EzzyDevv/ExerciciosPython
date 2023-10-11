from time import sleep
from subprocess import run


while True:
    answer = int(input(("Qual número deseja ver a tabuada ? Caso negativo, programa será encerrado!\n>>> ")))
    
    if answer < 0:
        print("Saindo...\nAté logo!")
        break
    else:
        for x in range(0, 11):
            print(f"{answer} x {x} = {answer * x}")
    sleep(4)
    run('cls | clear', shell=True)