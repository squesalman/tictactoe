# Game Logic : 
# 1. choose x or o
# 2. placement x or o based on number 1 - 9 at the grid
# 3. once player choose check if selected grid is available or not available or player already enter there
# 4. place marker and display board
# 5. repeat 1-4 till full
# 6. Check who wins
# 7. End and prompt to restart or no

import random

#Step 1
def player_marker():
    choice = 'ss'
    while choice not in ['X','O']:
        choice = input("Please enter your marker X or O : ").upper()
        if choice not in ['X','O']:
          print("Please enter valid marker X or O")
    if choice == 'X':
      return ('X','O')
    else:
      return ('O','X')

#Step 2
def display_board(boardlist):
  print(f"{boardlist[0]}|{boardlist[1]}|{boardlist[2]}")
  print("-----")
  print(f"{boardlist[3]}|{boardlist[4]}|{boardlist[5]}")
  print("-----")
  print(f"{boardlist[6]}|{boardlist[7]}|{boardlist[8]}")

# Step 3
def board_placement(boardlist):
  marker_placement = 'wrong'
  while marker_placement not in ['1','2','3','4','5','6','7','8','9']:
    marker_placement = input('please enter your desired position from 1-9')
  
    try:
      val = int(marker_placement)
      if val > len(boardlist):
        print(val)
    except ValueError:
      print('please enter number in range 1-9')
    #Need to have exception handling when number is out of bound
    except IndexError:
      print('Value if out of bound of the index')
    else:
      if boardlist[int(marker_placement)-1] in ['X','O']:
        print('position occupied. Please choose different number')
        marker_placement = 'wrong'
      # if 'X' in boardlist[int(marker_placement)-1]:
      #   print('position occupied. Please choose different number')
      #   marker_placement = 'wrong'
      # elif 'O' in boardlist[int(marker_placement)-1]:
      #   print('position occupied. Please choose different number')
      #   marker_placement = 'wrong'
  #print('\n'*100)   
  return int(marker_placement)-1
  
  


#Step 4
def new_board(boardlist,position,marker):
  boardlist[position] = marker
  return boardlist

def check_win(board,mark):
  return board[0] == mark and board[1] == mark and board[2]== mark or board[3] == mark and board[4] == mark and board[5]== mark or board[6] == mark and board[7] == mark and board[8]== mark or board[0] == mark and board[3] == mark and board[6]== mark or board[1] == mark and board[4] == mark and board[7]== mark or board[2] == mark and board[5] == mark and board[8]== mark or board[0] == mark and board[4] == mark and board[8]== mark or board[2] == mark and board[4] == mark and board[6]== mark

def choose_first():
  if random.randint(0, 1) == 0:
    return 'Player 1'
  else:
    return 'Player 2'


# def space_check(board,position):
#   if 'x' in board[position]:
#     return False
#   elif 'o' in board[position]:
#     return False
#   else:
#     return True


def full_board_check(board):
  full = True
  for item in board:
    if '' in board:
      full = False
  return full


def replay():
  choice = 'wrong'

  while choice not in ['Y','N']:

    choice = input('Would like to play again? Please press Y or N ' ).upper()
    if choice not in ['Y','N']:
      print('Please enter a valid input Y or N')
    
  if choice == 'Y':
    return True
  else:
    return False


if __name__ == "__main__":
    print('WELCOME to TIC TAC TOE')

    while True:
        
      game_board = ['']*10
      player1,player2 = player_marker()
      turn = choose_first()
      print (f'{turn} will go first')

      play_game = input('Are you ready to play? Enter Yes or No.')
      
      #Need to have exception handling if user input other than y or n
      if play_game.lower()[0] == 'y':
          game_on = True
      else:
          game_on = False
      
      while game_on:
        if turn == 'Player 1':
          #Player1 turn
          display_board(game_board)
          position = board_placement(game_board)
          new_board(game_board,position,player1)

          if check_win(game_board,player1):
            display_board(game_board)
            print('You have won the game!')
            game_on = False
          else:
            if full_board_check(game_board):
              display_board(game_board)
              print('Game is a draw')
              break
            else:
              turn = 'Player 2'
        else:
          #Player2 turn
          display_board(game_board)
          position = board_placement(game_board)
          new_board(game_board,position,player2)

          if check_win(game_board,player2):
            display_board(game_board)
            print('You have won the game!')
            game_on = False
          else:
            if full_board_check(game_board):
              display_board(game_board)
              print('Game is a draw')
              break
            else:
              turn = 'Player 1'
      if not replay():
        break
      




        
        


# board = ['X', 'O', '', 'X', 'X', 'X', 'X', 'X', 'O']
# position = board_placement(board)
# #new_board = new_board(board,position,'x')
# #spacechecker = space_check(board,position)
# fullchecker = full_board_check(board)
# win = check_win(board,'x')
# test_replay = replay()
# player1 = player_marker()

