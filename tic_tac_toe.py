import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
display_board = ['|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|', '|___|']

turn = 0


def is_winner():
    winner = False
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]):
        winner = True
    elif (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]):
        winner = True
    elif (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        winner = True
    else:
        winner = False
    return winner


def render_display_board():
    display_rows = [display_board[x:x+3] for x in range(0, len(display_board), 3)]
    for row in display_rows:
        print(''.join(row))


# def circles_turn():
#     placement = int(input("CIRCLE: Pick a square: "))
#     if placement in board:
#         board[placement - 1] = 'O'
#         display_board[placement - 1] = '| O |'
#     else:
#         print("That square is already chosen.")
#         circles_turn()

def circles_turn():
    placement = random.randint(1, 9)
    print("CIRCLE picks {}".format(placement))
    if placement in board:
        board[placement - 1] = 'O'
        display_board[placement - 1] = '| O |'
    else:
        print("That square is already chosen.")
        circles_turn()

def crosses_turn():
    placement = int(input("CROSS: Pick a square: "))
    if placement in board:
        board[placement - 1] = 'X'
        display_board[placement - 1] = '| X |'
    else:
        print("That square is already chosen.")
        crosses_turn()


while turn < 9:
    render_display_board()
    odd = turn % 2 != 0
    if odd:
        circles_turn()
        game_over = is_winner()
        if game_over:
            render_display_board()
            print("O's WIN")
            break
        else:
            turn += 1
            continue
    else:
        crosses_turn()
        game_over = is_winner()
        if game_over:
            render_display_board()
            print("X's WIN")
            break
        else:
            turn += 1
            continue


