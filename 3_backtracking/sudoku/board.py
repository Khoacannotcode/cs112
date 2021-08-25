class Board():
  def __init__(self):
    self.board = None

  def read_From_String(self, string):
    """
    Make a board from a string

    Input:
    --string : The input string
    Output (Optional):
    --board : Board after reading
    """
    board = []
    for i in range(len(string)):  
        if i % 9 == 0:
            temp = []
            for j in string[i:i+9]:
                temp.append(int(j))
            board.append(temp)
    self.board = board
    return board

  def as_String(self):
    """
    Convert a board to a string representation

    Input:
    --board : a board to convert
    Ouput:
    --string : a string representation
    """
    return ''.join(map(str,[''.join(map(str, i)) for i in self.board]))

  def draw(self, name = None):
    """
    Draw the board
    """
    if name:
      print("> {}".format(name))
    if not self.board:
      print("board is None!")
    for r in range(len(self.board)):
        if r == 0 or r == 3 or r == 6:
            print("+-------+-------+-------+")
        for c in range(len(self.board[r])):
            if c == 0 or c == 3 or c ==6:
                print("| ", end = "")
            if self.board[r][c] != 0:
                print(self.board[r][c], end = " ")
            else:
                print(end = "  ")
            if c == 8:
                print("|")
    print("+-------+-------+-------+")