# connect_four.py

import numpy as np


def hit(x, player):
    i = 0
    hit = 0
    while i in range(0, len(x)) and hit < 4:
        if x[i] == 0:
            i += 1
            hit = 0
        elif x[i] == player:
            i += 1
            hit += 1
        else:
            i += 1
            hit = 0
    return hit == 4


def check_winner(player, board):
    s = False
    if s is False:
        for i in range(0, 6):
            z = board[i]  # row search 0 to 6
            s = hit(z, player)
            if hit(z, player) is True:
                s = True
                return s
            else:
                continue
        for i in range(0, 7):
            w = [row[i] for row in board]  # column search 0 to 5
            s = hit(w, player)
            if hit(w, player) is True:
                s = True
                return s
            else:
                continue
        for i in range(-2, 4):
            y = np.diagonal(
                board, i
            )  # -2 to 3 scans diagonally from second row 0 to the first row column four
            s = hit(y, player)
            if hit(y, player) is True:
                s = True
                return s
            else:
                continue
        for i in range(-2, 4):
            x = np.fliplr(board).diagonal(i)  # Flip the board over the y axis
            s = hit(x, player)
            if hit(x, player) is True:
                s = True
                return s
            else:
                continue


def print_winner(board):
    print(*board, sep="\n")
    if check_winner(1, board) is True:
        print("Player 1 wins!")
    else:
        if check_winner(2, board) is True:
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


# Player 1 wins
def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    # Player 2 wins
    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    # No winner yet
    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


main()
