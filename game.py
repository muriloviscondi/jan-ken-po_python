class Game:

    __score_player: int = 0
    __score_cpu: int = 0

    def move_game(self, move):
        if move == 1:
            return "Pedra"
        elif move == 2:
            return "Papel"
        elif move == 3:
            return "Tesoura"

    def checked_win_lose(self, player, cpu):
        if player == cpu:
            return 'Empate!'
        elif player == 1 and cpu == 3:
            return 'Player vence!'
        elif player == 2 and cpu == 1:
            return 'Player vence!'
        elif player == 3 and cpu == 2:
            return 'Player vence!'
        else:
            return 'CPU vence!'

    def score_player(self, player, cpu):
        checked = self.checked_win_lose(player, cpu)
        if checked == 'Player vence!':
            self.__score_player += 1
            return self.__score_player
        else:
            return self.__score_player

    def score_cpu(self, player, cpu):
        checked = self.checked_win_lose(player, cpu)
        if checked == 'CPU vence!':
            self.__score_cpu += 1
            return self.__score_cpu
        else:
            return self.__score_cpu
