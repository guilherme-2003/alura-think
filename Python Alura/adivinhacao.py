import random 

def jogo():

    print('*' * 32)
    print('Bem vindo ao jogo da adivinhação')
    print('*' * 32)

    num_secreto = random.randint(1, 100) 
    tentativas = 0
    nivel = 0
    pontos = 1000

    while(nivel != 1 and nivel != 2 and nivel != 3):
        print('Escolha um nível de dificuldade: ')
        nivel = int(input('(1) - Fácil\n(2) - Médio\n(3) - Difícil\n> '))

        if(nivel == 1):
            tentativas = 20
        elif(nivel == 2):
            tentativas = 10
        elif(nivel == 3):
            tentativas = 5
        else:
            print('Nível de dificuldade inválido!\n')

    print(num_secreto)

    for rodada in range(1, tentativas + 1):
        print(f"\nTentativa {rodada} de {tentativas}\n")
        chute = int(input('Digite um número entre 1 e 100: '))

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        print(f'\nVocê digitou {chute}')

        if(chute == num_secreto):
            print(f'Vocề acertou! Você fez {pontos} pontos!')
            break
        else:
            if(chute > num_secreto):
                print('Você errou! O seu chute foi maior que o número secreto')
            else:
                print('Você errou! O seu chute foi menor que o número secreto')
            pontos_perdidos = abs(num_secreto - chute)
            pontos -= pontos_perdidos
        rodada += 1
        
    print('\nFIM DO JOGO!\n')

if(__name__ == '__main__'):
    jogo()