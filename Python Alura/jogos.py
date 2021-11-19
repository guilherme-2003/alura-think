import forca
import adivinhacao

print('*' * 16)
print('Escolha um jogo!')
print('*' * 16)

jogo = int(input('(1) - Forca\n(2) - Adivinhação\n> '))

if(jogo == 1):
    print('\nAbrindo jogo da forca...\n')
    forca.jogo()
elif(jogo == 2):
    print('\nAbrindo o jogo da adivinhação...\n')
    adivinhacao.jogo()