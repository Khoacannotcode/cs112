from board import Board
from backtrackingSudoku import BacktrackingSudokuSolver
from sudokuLoader import Sudoku_Loader

import argparse
import time
import os
import numpy as np

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
                    help="Find the first answer"
)
parser.add_argument('--solve_all',
                    type=bool,
                    default=False,
                    help="Find all answer"
)
parser.add_argument('--gen_with_rank',
                    type=int,
                    default=False,
                    help="auto gen blank board and find the answer"
)
args = parser.parse_args()

# Driver Code
def main():
  os.system('cls')
  if args.gen_with_rank:
    string = "0"*args.gen_with_rank**4
    puzzle_list = [string]
    GT_list = [string]
  else:
    dataloader = Sudoku_Loader()
    puzzle_list, GT_list = dataloader.load_From_Path(args.data_path)
  size = int(np.sqrt(np.sqrt(len(puzzle_list[0]))))

  if args.solve_all:
    puzzle_string = puzzle_list[0]
    GT_string = GT_list[0]
    board = Board(size=size)
    board.read_From_String(puzzle_string)
    board.draw(name="Solve all for")
    solver = BacktrackingSudokuSolver(size=size)
    solver.solve_All(board)
    return

  for idx in range(len(puzzle_list)):
    puzzle_string = puzzle_list[idx]
    GT_string = GT_list[idx]
    board = Board(size=size)
    board.read_From_String(puzzle_string)
    print("Test case {}".format(idx+1))
    if args.show:
      board.draw()
    solver = BacktrackingSudokuSolver(size=size)
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

main()