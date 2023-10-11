tabela = ("Banana", 4.99, 
          "Maçã", 8.99, 
          "Abacaxi", 3.50, 
          "Abacate", 2.79,
          "Abacate", 2,
          "Melancia", 14.9)

print("=" * 52)
print(f"|| {'TABElA DE PREÇOS':^45}  ||")
print("=" * 52)
for x in range(0, len(tabela), 2):
  print(f"{tabela[x]:.<43}R${tabela[x + 1]:>7.2f}")
print("=" * 52)