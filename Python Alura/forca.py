def jogo():
            
    print('*' * 26)
    print('Bem vindo ao jogo da forca')
    print('*' * 26)

    palavra_secreta = 'laranja'.upper()
    letras_acertadas = ['-' for _ in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    tamanho_da_palavra = len(palavra_secreta)
    
    print( '_' * 4)
    print('|  |')
    print('|  O')
    print('| /|\\')
    print('| / \\\n')

    print('- ' * tamanho_da_palavra)

    while(not enforcou and not acertou):
        chute = input('Digite uma letra: ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0 
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1  

        enforcou = erros == 6
        acertou = '-' not in letras_acertadas
        print(str(letras_acertadas))

    if(acertou):
        print('\nParabéns! Você acertou!\n')
    else:
        print('\nGame Over! Você errou!\n')

if(__name__ == '__main__'):
    jogo()