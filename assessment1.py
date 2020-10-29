def main():
  
  while True:
    intro()
    
    break

def intro():
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


  

def play_game():
  position = ['x','o','x']
  print(f"{position[0]}|\t | ")

main()
