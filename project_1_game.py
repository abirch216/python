"""Author: Alexander Birchfield"""

import random


def display_board(board):
    """ displays the tic tac board"""
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


def player_input():
    """ask the user if they would like to be x's or o's"""
    choice = input("Player 1: Would you like to be 'X' or 'O'? ").upper()
    while choice != 'X' and choice != 'O':
        choice = input("Invalid choice! Would you like to be X or O? ").upper()
    return choice


def place_marker(board, marker, position):
    """places the x or o on the board"""
    board[position] = marker


def win_check(board, mark):
    """checks to see if one of the players has won by getting 3 in a row"""
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


def choose_first():
    """randomly selects if player1 or player2 goes first"""
    first = random.randint(1, 2)
    if first == 1:
        return "player1"


def space_check(board, position):
    """checks to see the position is open on the board"""
    return board[position] == " "


def full_board_check(board):
    """checks to see if every spot on the board is taken"""
    for space in range(1, len(board)):
        if board[space] == " ":
            return False
    return True


def player_choice(board):
    """ask the user where they would like to place their marker"""
    choice = int(input("Where would you like to place your marker (1-9)? "))
    while choice < 1 or choice > 9:
        choice = int(input("Out of range! Where would you like to place your marker (1-9)? "))

    open_space = space_check(board, choice)
    if open_space:
        return choice
    else:
        while not open_space or choice < 1 or choice > 9:
            choice = int(input("Position is already taken! "
                               "Where would you like to place your marker (1-9)? "))
            while choice < 1 or choice > 9:
                choice = int(input("Out of range! Where would you like to place your marker "
                                   "(1-9)? "))
            open_space = space_check(board, choice)
        return choice


def replay():
    """asks the user if they would like to play again"""
    choice = input("Would you like to play again? (yes or no): ").lower()
    while choice != 'yes' and choice != 'no':
        choice = input("Invalid choice! Would you like to play again? (yes or no) ").lower()
    if choice == 'yes':
        return True
    else:
        print("Goodbye!")
        return False


while True:
    print("Welcome to Tic Tac Toe!")

    player1 = player_input()

    if player1 == "X":
        print("Player 2 you are 'O'")
        player2 = "O"
    else:
        print("Player 2 you are 'X'")
        player2 = "X"

    if choose_first() == "player1":
        player_first = player1
        player_second = player2
        print("Player 1 will go first.")
    else:
        player_first = player2
        player_second = player1
        print("Player 2 will go first")

    test_board = [" "] * 10
    display_board(test_board)

    while True:

        while True:
            try:
                player_spot = player_choice(test_board)
            except ValueError:
                print("You must input an interger!")
                continue
            else:
                break
        place_marker(test_board, player_first, player_spot)
        if win_check(test_board, player_first):
            display_board(test_board)
            print(f"Congrats! '{player_first}' has won the game!")
            break
        elif full_board_check(test_board):
            display_board(test_board)
            print("The game is a tie!")
            break
        display_board(test_board)
        while True:
            try:
                player_spot = player_choice(test_board)
            except ValueError:
                print("You must input an interger!")
                continue
            else:
                break
        place_marker(test_board, player_second, player_spot)
        if win_check(test_board, player_second):
            display_board(test_board)
            print(f"Congrats! '{player_second}' has won the game!")
            break
        elif full_board_check(test_board):
            display_board(test_board)
            print("The game is a tie!")
            break
        display_board(test_board)

    if not replay():
        break
