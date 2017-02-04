from Controller import *

class Game:



    def __init__(self):
        self.controller = Controller()
        self.board = Board()

    def play_game(self):
        while True:
            stone_index = self.controller.get_stone_index()
            self.controller.add_stone_to_board(stone_index)
            self.controller.print_board()
            if self.controller.check_winning_conditions():
                break
            self.controller.change_turn()

        print 'Player ' + self.controller.players[self.controller.turn].get_stone_sign()  + ' wins'



if __name__ == '__main__':
    game = Game()
    game.play_game()