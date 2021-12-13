with open ('nomes.txt', 'r') as arquivo:
    ler_arquivo = [item.split()[0] for item in arquivo]

lista_usuarios = ['usuario@'+ nome for nome in ler_arquivo if len(nome) >= 3]
print(lista_usuarios)