from board import Board
from backtrackingSudoku import BacktrackingSudokuSolver
from sudokuLoader import Sudoku_Loader

import argparse
import time
import os

parser = argparse.ArgumentParser(description='Sudoku Solver')
parser.add_argument('--method', 
                    type=str, 
                    help="""
                    Choose the method to use:
                    - brute force
                    - greedy
                    - backtracking
                    """
)
parser.add_argument('--data_path', 
                    type=str, 
                    help="Path to the txt file"
)
parser.add_argument('--show',
                    type=bool,
                    default=False,
                    help="show the sudoku boards"
)
args = parser.parse_args()

# Driver Code
os.system('cls')
dataloader = Sudoku_Loader()
puzzle_list, GT_list = dataloader.load_From_Path(args.data_path)

for idx in range(len(puzzle_list)):
  puzzle_string = puzzle_list[idx]
  GT_string = GT_list[idx]
  board = Board()
  board.read_From_String(puzzle_string)
  print("Test case {}".format(idx+1))
  if args.show:
    board.draw()
  solver = BacktrackingSudokuSolver()
  t0 = time.time()
  solver.solve(board)
  t1 = time.time()
  if args.show:
    board.draw(name="Answer:")
  if board.as_String() == GT_string:
    print("✔ Passed!")
  else:
    print("❌ Wrong Answer!")
  print("Running time = {}".format(t1-t0))
  print("\n")
