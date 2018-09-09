from random import randint
import time
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('''Qual é a sua jogada?
[0] Pedra
[1] Papel
[2] Tesoura
'''))
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÕ')
computador = randint(0,2)
print('-=-' * 11)
print('Computador escolheu {}'.format(itens[computador]))
print('-=-' * 11)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você venceu.')
    else:
        print('Você perdeu.')

elif computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você venceu.')
    else:
        print('Você perdeu.')

elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('Você venceu.')
    else:
        print('Você perdeu.')
