import os
from random import randint
from time import sleep

from game import Game

game = Game()

player: int = 0
cpu: int = 0

while True:
    print(
        f'====== PLAYER {game.score_player(player,cpu)} '
        f'X '
        f'{game.score_cpu(player, cpu)} CPU ======='
    )

    print(
        'Escolha a sua opção'
        '\nPedra   [1]'
        '\nPapel   [2]'
        '\nTesoura [3]'
    )

    player: int = int(input('Digite sua opção: '))
    cpu: int = randint(1, 3)

    while player < 1 or player > 3:
        print('Opção inválida!')
        player: int = int(input('Digite sua opção: '))

    print(
        f'Player joga {game.move_game(player)} x {game.move_game(cpu)} joga PC'
        f'\n{game.checked_win_lose(player, cpu)}'
    )

    print('=' * 31)
    sleep(1)
