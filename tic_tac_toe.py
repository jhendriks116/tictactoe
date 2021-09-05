#To print the game board
the_board = {'7' : ' ', '8' : ' ', '9' : ' ',
             '4' : ' ', '5' : ' ', '6' : ' ',
             '1' : ' ', '2' : ' ', '3' : ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#To define the game space
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(the_board)
        print("It's your turn, " + turn + ". Enter tile to move to:")
        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count +=1
        else:
            print("That tile is already filled.\n Please choose another tile")
            continue

        if count >= 5:
            #To check if across the top is a winner
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check if across the middle is a winner
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check if across the bottom is a winner
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check if down the left is a winner
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check if down the middle is a winner
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check if down the right is a winner
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check if diagonally is a winner
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break
            #To check is diagonally is a winner
            elif the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                print_board(the_board)
                print("Game Over!")
                print(turn + ' wins!')
                break

        #To chek for a draw
        if count == 9:
            print('Game Over!')
            print("It's a Draw!")

        # To change turns
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    #To ask players if they want to restart the game
    restart = input("Do you want to play again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            the_board[key] = ' '

        game()

if __name__ == "__main__":
    game()