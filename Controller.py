from Player import *
from Board import *

class Controller:

    def __init__(self):
        self.turn = 0
        self.players = []
        self.players.append(Player('x'))
        self.players.append(Player('o'))
        self.stones = [['.' for x in range(4)] for y in range(4)]

    def change_turn(self):
        self.turn = (self.turn + 1) % 2

    def get_stone_index(self):
        while(True):
            stone_index = raw_input('Player ' + self.players[self.turn].get_stone_sign() + ':')
            if self.check_index_correction(stone_index) and self.check_board_space(stone_index):
                break
            else:
                continue
        return stone_index

    def check_index_correction(self, stone_index):
        if len(stone_index) != 3:
            return False

        s = stone_index.split(' ')
        if (ord(s[0]) < 48 or ord(s[0]) > 51) or (ord(s[1]) < 48 or ord(s[1]) > 51):
            return False
        else:
            return True

    def check_board_space(self, stone_index):
        pos = [int(x) for x in stone_index.split(' ')]
        if self.stones[pos[0]][pos[1]] is '.':
            return True
        else:
            return False

    def add_stone_to_board(self, stone_index):
        pos = [int(x) for x in stone_index.split(' ')]
        self.stones[pos[0]][pos[1]] = self.players[self.turn].get_stone_sign()

    def print_board(self):
        Board.draw_board(self.stones)

    def check_winning_conditions(self):
        playing_stone = self.players[self.turn].get_stone_sign()
        opposite_stone = self.players[(self.turn+1)%2].get_stone_sign()
        for x in range(4):
            for y in range(4):
                surrounding_stones = 0
                if self.stones[x][y] is opposite_stone:
                    back_x = x - 1
                    back_y = y - 1
                    up_x = x + 1
                    up_y = y + 1
                    if back_x > -1:
                        if self.stones[back_x][y] is playing_stone:
                            surrounding_stones += 1
                    else:
                        surrounding_stones +=1

                    if back_y > -1:
                        if self.stones[x][back_y] is playing_stone:
                            surrounding_stones += 1
                    else:
                        surrounding_stones += 1

                    if up_x < 4:
                        if self.stones[up_x][ y] is playing_stone:
                            surrounding_stones += 1
                    else:
                        surrounding_stones += 1

                    if up_y < 4:
                        if self.stones[x][up_y] is playing_stone:
                            surrounding_stones += 1
                    else:
                        surrounding_stones += 1

                if surrounding_stones == 4:
                    return True
        return False