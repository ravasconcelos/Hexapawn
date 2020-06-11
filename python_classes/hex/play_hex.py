from six.moves import input
from hextypes import Player, Point
from hexboard import *
from minimax import *

COL_NAMES = 'ABC'


def print_board(board):
    print('   A   B   C')
    for row in (1, 2, 3):
        pieces = []
        for col in (1, 2, 3):
            piece = board.get(Point(row, col))
            if piece == Player.x:
                pieces.append('X')
            elif piece == Player.o:
                pieces.append('O')
            else:
                pieces.append(' ')
        print('%d  %s' % (row, ' | '.join(pieces)))


def point_from_coords(text):
    col_name_a = text[0]
    row_a = int(text[1])
    col_name_b = text[2]
    row_b = int(text[3])
    return Point(row_a, COL_NAMES.index(col_name_a) + 1), Point(row_b, COL_NAMES.index(col_name_b) + 1)


def main():
    game = GameState.new_game()

    human_player = Player.x

    bot = MinimaxAgent()

    while not game.is_over():
        print_board(game.board)
        if game.next_player == human_player:
            human_move = input('-- ')
            point_a, point_b = point_from_coords(human_move.strip())
            move = Move(point_a, point_b)
            if not game.is_valid_move(move):
                print('Not a valid move')
                continue
        else:
            move = bot.select_move(game)
            if move is None:
                print('Should have a move :-(')
        game = game.apply_move(move)

    print_board(game.board)
    winner = game.winner()
    print('Winner: ' + str(winner))


if __name__ == '__main__':
    main()
