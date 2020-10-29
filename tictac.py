# Game Logic : 
# 1. choose x or o
# 2. placement x or o based on number 1 - 9 at the grid
# 3. once player choose check if selected grid is available or not available or player already enter there
# 4. place marker and display board
# 5. repeat 1-4 till full
# 6. Check who wins
# 7. End and prompt to restart or no

#Step 1
def player_input():
  pl2 = ''
  while True:
    pl1 = input("First player Enter 'x' or 'o' only : ").upper()
    if pl1.upper() == 'X' or pl1.upper() == 'O':
      print("Accepted")
      if pl1.upper() == 'X':
        pl2 = 'O'
      else:
        pl2 = 'X'
      break
    else:
      print("Please enter correct marker")
  print(f"welcome {pl1} and {pl2}")

#Step 2
def draw_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

#Step 3
def place_marker(board,marker,position):
  board[position]=marker

#Step 4
def check_win(board,mark):
  return board[0] == mark and board[1] == mark and board[2]== mark or board[3] == mark and board[4] == mark and board[5]== mark


def play_game():
  position_list = ['1','2','3','4','5','6','7','8','9']
  while True:
    position = int(input("Please enter your position from 1-9: "))
    if position > 9 or position < 0:
      print("please enter number ranging 1-9 only")
    else:
      position_list[position-1] = 'x'
      draw_board(position)
    break

def main():
  while True:
    player_input()
    play_game()
    break
  



test_draw = ['x','x','o','x','o','x','o','x','p']
mark = 'x'
place_marker(test_draw,'$$',8)
draw_board(test_draw)
print(check_win(test_draw,'x'))

