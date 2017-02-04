
class Board:

    @staticmethod
    def draw_board(stones):
        print '/----\\'
        for x in range(4):
            row = '|'
            for y in range(4):
                row += stones[x][y]
            row +='|'
            print row
        print '\----/'




