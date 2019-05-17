import random

def init_board():
  return [' ',' ',' ',
          ' ',' ',' ',
          ' ',' ',' ']

def instructions():
  print("Here are the instructions\n")
  print(" 1 | 2 | 3 ")
  print("------------")
  print(" 4 | 5 | 6 ")
  print("------------")
  print(" 7 | 8 | 9 ")

def print_board(board):
  print(" %s | %s | %s " %(board[0], board[1], board[2]))
  print("------------")
  print(" %s | %s | %s " %(board[3], board[4], board[5]))
  print("------------")
  print(" %s | %s | %s " %(board[6], board[7], board[8]))


def check_diagonal(board):
  # Check left to right diagonal
  if (board[0] != ' ' and board[0] == board[0+4] == board[len(board)-1]):
    return board[0]
  if (board[2] != ' ' and board[2] == board[4] == board[6]):
    return board[2]
  return 0
  return 0

def check_row(board):
  for x in range(3):
    if (board[x] != ' ' and board[x] == board[x+1] == board[x+2]):
      return board[x]
  return 0

def check_column(board):
  for x in range(3):
    if (board[x] != ' ' and board[x] == board[x+3] == board[x+6]):
      return board[x]
  return 0

def check_board(board):
  if (check_diagonal(board) == 'O' or check_row(board) == 'O' or check_column(board) == 'O'):
    return 'O'
  if (check_diagonal(board) == 'X' or check_row(board) == 'X' or check_column(board) == 'X'):
    return 'X'
  return 0


def main():
  # Print out the instructions
  instructions()
  # Initialize the game board
  board = init_board()
  moves = 9

  # Randomizes 'O' and 'X'
  turns = ['O', 'X']
  random.shuffle(turns)
  # Grab the user's input and starts the game. Player always starts
  while (check_board(board) == 0 and moves != 0):
    if (moves%2 == 1):
      print("Player's turn. (", turns[moves%2], ")",sep = '')
      while (True):
        try:
          user_input = int(input("Enter your choice: "))
          if (user_input not in range(0,10)):
            raise ValueError
          break
        except ValueError:
          print("Please enter a number from 1 - 9")
      choice = user_input-1
      if (board[choice] == ' '):
        board[choice] = turns[moves%2]
        moves -= 1
      else:
        print("Position already taken. Please input a different choice.")
        print_board(board)
    # Computer's turn
    else:
      print("Computer's turn (", turns[moves%2], ")", sep = '')
      choice = random.randint(0,8)
      while (board[choice] != ' '): 
        choice = random.randint(0,8)
      board[choice] = turns[moves%2]
      print("Computer has place an", turns[moves%2], "at cell #", choice+1)
      moves -= 1

    
    print_board(board)



  # Exited the loop. Print the game's summary.
  if (check_board(board) == 0):
    print("Draw Game")
  else:
    # Check if moves%2 is 0 since moves has decremented after the winning move
    if (moves%2 == 0):
      print("Player has won! (", check_board(board), ")", sep = '')
    else:
      print("Computer has won! (", check_board(board), ")", sep = '')


if __name__ == "__main__":
    main()
