#Criar uma tupla com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol :
tabela = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "Grêmio",
    "Athletico-pr",
    "Red Bull Bragantino",
    "Fortaleza",
    "Cuiabá",
    "São Paulo",
    "Atlético-mg",
    "Cruzeiro",
    "Internacional",
    "Corinthians"
    "Goiás",
    "Bahia",
    "Santos",
    "Vasco",
    "Coritiba",
    "América-mg"
)

while True:
    resposta = int(input("""
[1] Ver 5 primeiros colocados da tabela
[2] Últimos 4 colocados da tabela
[3] Uma lista com os times em ordem alfabética
[4] Ver posição do time Flamengo
[5] Para Sair do Programa\n>>> """))

    if resposta == 1:
        print(tabela[0:5])
    elif resposta == 2:
        print(tabela[-4:])
    elif resposta == 3:
        alfabetica = sorted(tabela)
        print(alfabetica)
    elif resposta == 4:
        print("O time do Flamengo se encontra na posição {}".format(tabela.index(("Flamengo")) + 1))
    elif resposta == 5:
        break
    else:
        print("Digite novamente...")