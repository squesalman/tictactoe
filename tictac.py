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
        choice = input("Please enter your marker X or O : ")
        choice = choice.upper()

        if choice not in ['X','O']:
            print("Please enter valid marker X or O")
    return choice
  

#Step 2
def draw_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

#Step 3
def place_marker(board,marker,position):
  board[position-1]=marker

#Step 4
def check_win(board,mark):
  return board[0] == mark and board[1] == mark and board[2]== mark or board[3] == mark and board[4] == mark and board[5]== mark or board[6] == mark and board[7] == mark and board[8]== mark or board[0] == mark and board[3] == mark and board[6]== mark or board[1] == mark and board[4] == mark and board[7]== mark or board[2] == mark and board[5] == mark and board[8]== mark or board[0] == mark and board[4] == mark and board[8]== mark or board[2] == mark and board[4] == mark and board[6]== mark

#Step 5
def choose_first():
  return random.randint(1,2)

#Step 6
def space_check(board,position):
  if not board[position-1]:
    return 'position available'
  else:
    return 'choose diff position'

#Step 7
def full_board_check(board):
  count = 0
  full = True
  while count < len(board):
    print(count)
    if not board[count]:
      full = False
      break
    count+=1
  return full

  


#Step 8
def player_choice(board):
  while True:
    choice = int(input("Please select position from 1-9"))
    if choice < 1 and choice > 9 :
      print("please enter number 1-9 only ")
    else:
      print(space_check(board,choice))
      break
  
  
    
  
  

#Step 9
def replay():
  pass



player_marker()
test_draws = ['','x','o','x','o','','x','x','x']
#mark = 'x'
#place_marker(test_draw,'$$',8)
# draw_board(test_draw)
# print(check_win(test_draw,'x'))
# print(choose_first())
print(space_check(test_draws,1))
print(full_board_check(test_draws))
player_choice(test_draws)

# for item in range(len(test_draws)):
#   print(f"{item} : {test_draws[item]}")
