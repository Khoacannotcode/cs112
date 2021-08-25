from board import Board
import copy

class BacktrackingSudokuSolver():
  def __init__(self, size):
    # The set contains all solution found
    self.solutions = []
    self.size = size
    self.length = size**2
  
  def find_Zero(self, board):
    """
    Find the first index of zero in the board.

    Input:
    --board : board to search
    Outout:
    --(row, col) : position of the first zero, if not found return False.
    """
    for row in range(self.length):
      if 0 in board[row]:
        col = board[row].index(0)
        return (row, col)
    return False

  def is_Valid(self, board, row, col, value):
    """
    Check if the value in position (row, col) is a valid or not.

    Input:
    --board : board to check
    --row : row to check
    --col : column to check
    --value : value to check
    Output:
    --True if valid
    --False if not valid
    """
    # Check row:
    for j in range(self.length):
      if board[row][j] == value:
        return False
    # Check column:
    for i in range(self.length):
      if board[i][col] == value:
        return False
    # Check block
    block_row = row // self.size
    block_col = col // self.size
    for i in range(self.size):
      for j in range(self.size):
        if board[self.size*block_row + i][self.size*block_col + j] == value:
          return False
    return True

  def solve(self, board):
    """
    Solve the Sudoku board using Backtracking Algorithm

    Input:
    --board : board after solving
    Output:
    --board : Solved board
    """
    cell = self.find_Zero(board.board)
    if not cell:
      return True
    else:
      row, col = cell
    for val in range(1,self.length + 1):
      if self.is_Valid(board.board, row, col, val):
        board.board[row][col] = val
        if self.solve(board):
          # self.solutions.add(board.to_String())
          return board
        # Trigger for backtracking
        board.board[row][col] = 0
    return False

  def solve_All(self, board):
    def solve_this(board):
      cell = self.find_Zero(board.board)
      if not cell:
        return True
      else:
        row, col = cell
      for val in range(1,self.length + 1):
        if self.is_Valid(board.board, row, col, val):
          board.board[row][col] = val
          if self.solve(board):
            board.draw()
            # tmp_board = copy.deepcopy(board)
            # self.solutions.append(tmp_board)
            # return board
          # Trigger for backtracking
          board.board[row][col] = 0
      return False
    solve_this(board)
    # return self.solutions