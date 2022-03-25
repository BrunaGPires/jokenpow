from random import randint
from time import sleep

rodada = 1
tentativa = 3
while (tentativa > 0):

    jogador_vence = comp_vence = empate = 0
    opcoes = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)

    lista = [0,1,2]
    jogador = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nEscolha sua jogada: '))
    print('Rodada {} de {}'.format(rodada, tentativa))
    tentativa = tentativa - 1
    while jogador not in lista:
        jogador = int(input('Digite um valor valido [0] [1] [2]. Qual a sua jogada? '))

    print('\033[31mJO]\033[m')
    sleep(.3)
    print('\033[31mKEN]\033[m')
    sleep(.3)
    print('\033[31mPO!]\033[m')
    print('-=' * 12)
    print(f'Computador jogou {opcoes[computador]}')
    print(f'Jogador jogou {opcoes[jogador]}')
    print('-=' * 12)

    if computador == 0: #computador jogou pedra
        if jogador == 0:
            print('Empate!')
            empate += 1
        elif jogador == 1:
            print('Jogador venceu!')
            jogador_vence +=1
        elif jogador == 2:
            print('Computador venceu!')
            comp_vence += 1

    elif computador == 1: #papel
        if jogador == 0:
            print('Computador venceu!')
            comp_vence += 1
        elif jogador == 1:
            print('Empate!')
            empate += 1
        elif jogador == 2:
            print('Jogador venceu!')
            jogador_vence += 1

    elif computador == 2: #tesoura
        if jogador == 0:
            print('Jogador venceu!')
            jogador_vence += 1
        elif jogador == 1:
            print('Computador venceu!')
            comp_vence += 1
        elif jogador == 2:
            print('Empate!')
            empate +=1



