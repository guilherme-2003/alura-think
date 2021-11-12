soma_dos_elementos = [] #Cria uma lista e armazena na variável soma_dos_elementos

num1 = int(input('Digite o primeiro número: ')) #Recebe um parâmetro de número inteiro passado pelo usuário e o armazena na variável "num1"
num2 = int(input('Digite o segundo número: ')) #Recebe um parâmetro de número inteiro passado pelo usuário e o armazena na variável "num2"
num3 = int(input('Digite o terceiro número: ')) #Recebe um parâmetro de número inteiro passado pelo usuário e o armazena na variável "num3"

soma_dos_elementos.append(num1) #Adiciona o valor armazenado na variável "num1" na posição 0 da lista
soma_dos_elementos.append(num2) #Adiciona o valor armazenado na variável "num2" na posição 1 da lista
soma_dos_elementos.append(num3) #Adiciona o valor armazenado na variável "num3" na posição 2 da lista

soma = sum(soma_dos_elementos) #Usa a função sum para somar todos os elementos da lista e armazena o valor na variável "soma"

print(soma_dos_elementos) #Printa a lista no terminal
print(f'{soma_dos_elementos[0]} + {soma_dos_elementos[1]} + {soma_dos_elementos[2]} = {soma}') #Printa o valor da variável soma no terminal