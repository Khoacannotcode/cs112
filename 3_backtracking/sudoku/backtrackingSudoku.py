from board import Board

class BacktrackingSudokuSolver():
  def __init__(self):
    # The set contains all solution found
    self.solutions = set()
  
  def find_Zero(self, board):
    """
    Find the first index of zero in the board.

    Input:
    --board : board to search
    Outout:
    --(row, col) : position of the first zero, if not found return False.
    """
    for row in range(9):
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
    for j in range(9):
      if board[row][j] == value:
        return False
    # Check column:
    for i in range(9):
      if board[i][col] == value:
        return False
    # Check block
    block_row = row // 3
    block_col = col // 3
    for i in range(3):
      for j in range(3):
        if board[3*block_row + i][3*block_col + j] == value:
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
    for val in range(1,10):
      if self.is_Valid(board.board, row, col, val):
        board.board[row][col] = val
        if self.solve(board):
          # self.solutions.add(board.to_String())
          return board
        # Trigger for backtracking
        board.board[row][col] = 0
    return False