a = [1, 2, 3] #Cria uma lista com três elementos e a armazena na variável "a"
b = [3, 2, 1] #Cria uma lista com três elementos e a armazena na variável "b"

pedro = 0 #Cria uma variável "pedro" de valor 0 que contabiliza a pontuação do jogador Pedro
paulo = 0 #Cria uma variável "paulo" de valor 0 que contabiliza a pontuação do jogador Paulo
i = 0 #Cria uma variável "i" de valor 0 que contabiliza o índice da lista

while i < 3: #Cria um laço while que, executa o bloco enquanto a variável "i" tiver valor menor que 3
    if a[i] > b[i]: #Cria um condicional if que confere se o elemento da lista "a" na posição "i" é maior que o elemento da lista "b" na posição "i"
        pedro += 1 #Soma 1 ao valor da variável "pedro" e armazena o novo valor na mesma variável caso a condição de if seja verdadeira
    elif a[i] < b[i]: #Cria um condicional elif que confere se o elemento da lista "a" na posição "i" é menor que o elemento da lista "b" na posição "i", que só executado caso a condição de if seja falsa
        paulo += 1 #Soma 1 ao valor da variável "paulo" e armazena o novo valor na mesma variável caso a condição de elif seja verdadeira
    i += 1 #Soma 1 ao valor da variável "i" e armazena o novo valor na mesma variável

with open("Pontuação.txt", "w") as arquivo: #Cria e escreve em um arquivo chamado "Pontuação" com a extensão .txt e na condição de escrita (w - write)
    arquivo.write(f"Pedro ganhou - {pedro} pontos!\nPaulo ganhou - {paulo} pontos!") #Mostra no arquivo Pontuação.txt a pontuação de Pedro e Paulo