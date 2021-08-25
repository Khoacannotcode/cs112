class Board():
  def __init__(self, size):
    self.board = None
    self.size = size
    self.length = size**2

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
        if i % self.length == 0:
            temp = []
            for j in string[i:i+self.length]:
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
        condition = [
                x for x in range(self.length)
                  if x%self.size == 0
                ]
        if r in condition:
            base = 2*self.size + self.size + 1
            line = self.size*("+" + "-"*base)
            line = line + "+"
            print(line)
        for c in range(len(self.board[r])):
            if c in condition:
                print("| ", end = "")
            if self.board[r][c] != 0:
                this_len = len(str(self.board[r][c]))
                if this_len == 1:
                  item = " {}".format(self.board[r][c])
                else:
                  item = self.board[r][c]
                print(item, end = " ")
            else:
                print("  ", end = " ")
            if c == self.length-1:
                print("|")
    print(line)