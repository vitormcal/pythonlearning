from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print ('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
 ''')
jogador = int(input('Qual será a sua jogada? '))
if jogador >= 3:
    print('Jogada INVÁLIDA!')
print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PO')
sleep(0.75)
print('-=' * 13)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 13)
if computador == 0: #O computador jogou Pedra
    if jogador == 0:
        print(('A partida empatou!'))
    elif jogador == 1:
        print(('O jogador venceu a partida!'))
    elif jogador == 2:
        print('O computador venceu a partida!')
elif computador == 1: #O computador jogou Papel
    if jogador == 0:
        print(('O computador venceu a partida!'))
    elif jogador == 1:
        print(('A partida empatou!'))
    elif jogador == 2:
        print('O jogador venceu a partida!')
elif computador == 2: #O computador jogou Tesoura
    if jogador == 0:
        print(('O jogador venceu a partida!'))
    elif jogador == 1:
        print(('O computador venceu a partida!'))
    elif jogador == 2:
        print('A partida empatou!')
