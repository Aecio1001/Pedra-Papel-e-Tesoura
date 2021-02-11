import random
moves = ['pedra', 'papel', 'tesoura']


class Player:

    def move(self):
        return 'pedra'

    def learn(self, my_move, their_move):
        pass


class Player(Player):

    def move(self):
    	return 'pedra'

class RandomPlayer(Player):

	def move(self):
		self.their_move = random.choice(moves)
		return self.their_move


class HumanPlayer(Player):

    def move(self):
        human = input("Digite sua jogada: ").lower()
        while human not in moves:
            human = input(f"{human} não é uma opção válida, por " +
                            "gentileza digite uma opção válida como: 'pe" +
                            "dra', 'papel', ou 'tesoura'.\n\nDigite sua" +
                            "jogada: ").lower()
        self.my_move = human
        return self.my_move


class ReflectPlayer(Player):

    def __init__(self):
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):

    def __init__(self):
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'pedra':
            return 'papel'
        elif self.my_move == 'papel':
            return 'tesoura'
        elif self.my_move == 'tesoura':
            return 'pedra'


class WinnerPlayer(Player):

    def __init__(self):
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        elif self.their_move == 'pedra':
            return 'papel'
        elif self.their_move == 'papel':
            return 'tesoura'
        elif self.their_move == 'tesoura':
            return 'pedra'


class Game:
    pr1 = 0
    pr2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Jogador: {move1}  Computador: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == 'pedra' and move2 == 'papel':
            self.pr2 += 1
            return (f"O computador ganhou por {self.pr2} e você tem" +
                    f"{self.pr1}!")
        elif move1 == 'pedra' and move2 == 'tesoura':
            self.pr1 += 1
            return (f"Você venceu por {self.pr1} a {self.pr2} do Computador!")
        elif move1 == 'tesoura' and move2 == 'papel':
            self.pr1 += 1
            return (f"Você venceu por {self.pr1} a {self.pr2} do Computador!")
        elif move1 == 'tesoura' and move2 == 'pedra':
            self.pr2 += 1
            return (f"O computador ganhou por {self.pr2} e você tem" +
                    f"{self.pr1}!")
        elif move1 == 'papel' and move2 == 'pedra':
            self.pr1 += 1
            return (f"Você venceu por {self.pr1} a {self.pr2} do Computador!")
        elif move1 == 'papel' and move2 == 'tesoura':
            self.pr2 += 1
            return (f"O computador ganhou por {self.pr2} e você tem" +
                    f"{self.pr1}!")
        else:
            self.pr1 += 1
            self.pr2 += 1
            return (f"a rodada ficou impatada! Você ganhou {self.pr1} e o " +
                    f"computador ganhou {self.pr2}!")

    def play_game(self):
        print("Jogo Iniciado!\n")
        roun = int(input("Digite quantas rodadas você deseja jogar: "))
        for round in range(roun):
            print(f"\nRodada {round}:")
            play = self.play_round()
            print(f'{play}\n')
        if self.pr1 > self.pr2:
            print(f"O Jogador venceu o jogo por {self.pr1} a {self.pr2} do" +
                  " Computador!")
        elif self.pr1 < self.pr2:
            print(f"O Computador venceu o jogo por {self.pr2} a {self.pr1}" +
                  " do Jogador!")
        else:
            print(f"O Jogado e o Computador ficaram impatados por" +
                  f" {self.pr1} a {self.pr2}!!")
        print("\nJogo Finalizado!")


if __name__ == '__main__':
    classes = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer(),
               WinnerPlayer()]
    classe = random.choice(classes)
    human = HumanPlayer()
    game = Game(human, classe)
    game.play_game()
