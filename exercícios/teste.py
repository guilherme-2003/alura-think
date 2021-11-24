from functools import reduce

teste = []
tamanho_da_lista = 3

while len(teste) < tamanho_da_lista: 
    teste.append(float(input("Digite um número: ")))

media = sum(teste) / tamanho_da_lista

print(f"A média é: {media:.2f}")