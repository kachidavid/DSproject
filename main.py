P = False
q = False
r = False


board = [
  [' ', ' ', ' ']
  [' ', ' ', ' ']
  [' ', ' ', ' '] 
]

def check_winners():
  for row in boards:
    if row[0] == row[1] == row [2] != ' ':
      return True
  for cols in range(3):
    if boards[0][cols] == boards[1][cols] == boards[2][cols] !=' ':
      return True

  if boards[0][0] == boards [1][1] == boards[2][2] != '':
    return True
  if boards [0][2] == boards[1][1] == boards[2][0] != ' ':
    return True
return False
  
  

