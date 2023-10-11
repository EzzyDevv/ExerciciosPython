anterior = 0
atual = 1
proximo = 1
c = 0

answer = int(input("Digite quantos termos da sequência de fibonacci deseja ver : "))
while c < answer:
    print(f"{anterior} ->", end=" ")
    if c == answer - 1:
        print("Fim")
        break
    
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    
    c += 1