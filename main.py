import random

rand_number = random.randint(1,5)
rodadas = 1
#tentativas  = 3
#new_game = 's'

def game():
    tentativas  = 3
    while(tentativas != 0):
        chute = int(input("Número: "))
        if(chute != rand_number):
            print('Não é esse')
            tentativas -= 1
        elif(chute == rand_number):
            print("Acertou!")
            break
    print('\nAcabaram as tentativas')


print(25*'*')
print('\tJogo de Adivinha')
print(25*'*')

print('\nTente adivinhar o número que o programa escolheu que está no intervalo de 1 a 5\nVocê terá 3 tentativas')

print('\nVamos lá!\n')
print(rand_number)

game()
new_game = input('\nMais uma rodada?(s/n) ')
if(new_game == 's'):
    game()
    rodadas += 1
elif(new_game == 'n'):
    print(f"\nInformações do jogador: \nRodadas: {rodadas}")

print('\nObrigado por jogar')
print(25*'*')