import random

rand_number = random.randint(1,5)
rodadas = 1
new_game = 's'

# Funções;
def main():
    welcome()
    game()

def welcome():
    print(35*'*')
    print('\tJogo de Adivinha')
    print(35*'*')

    print('\nTente adivinhar o número que o programa escolheu que está no intervalo de 1 a 5\nVocê terá 3 tentativas')

    print('\nVamos lá!\n')

def game():
    chute = 0
    tentativas  = 3
    while(chute != rand_number):
        chute = int(input("Número: "))
        if(chute != rand_number):
            print('Não é esse')
            tentativas -= 1
            if(tentativas == 0):
                print('\nAcabaram as tentativas')
                break
        else:
            print("É este o número!")
#

main()

while(new_game == 's'):
    new_game = input('\nMais uma rodada?(s/n) ')
    if(new_game == 's'):
        rodadas += 1
        rand_number = random.randint(1,5) 
        game()

print(f"\nInformações do jogador: \nRodadas: {rodadas}")

print('\nObrigado por jogar')
print(25*'*')
#