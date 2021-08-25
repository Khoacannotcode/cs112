# Framework cho backtracking
class BackTrackingSolver():
  def __init__(self):
    self.solutions = set()
  def solve(self, highest_value, safe_up_to, num_slots, display=False):
      solution = [None] * num_slots

      def solve_from(position):
          while True:
              if display:
                  displaySolution(solution)
              if safe_up_to(solution, position):
                  if position >= num_slots-1:
                      # We filled the last slot and everything is okay
                      # return solution
                      self.solutions.add("".join(str(x) for x in solution))
                      break
                  position += 1
                  solution[position] = 0
                  # if position < num_slots:
                  #     solution[position] = 0
                  # else:
                  #     break
              else:
                  # Backtrack. We might have to undo several slots, so....
                  while (solution[position] == highest_value-1):
                      solution[position] = None
                      position -= 1
                  if position < 0:
                      break
                  solution[position] += 1

          # We backtracked beyond the starting point, meaning we could not find
          # a valid value for the first slot, so no solution
          return None

      # With the iterative solution, I think you have to begin by priming the
      # solution list with the first value in the first slot.
      solution[0] = 0
      return solve_from(0)

def displaySolution(input_list):
  out_string = ""
  for item in input_list:
    if item != None:
      out_string += str(item)
    else:
      out_string += "_"
  print(out_string)
# Bài no-equal-adjancent substrings
# Hàm checker như sau
def checkSubstringsValid(string, up_to_index):
  # Kiểm tra xem liệu chuỗi từ 0 -> up_to_index có chứa bất kỳ chuỗi con kề nhau giống nhau nào hay không.
  # Chúng ta sẽ phải tử tất cả chuỗi con có length 1, 2, 3 cho đến độ dài nửa chuỗi.
  # Return False ngay khi chúng ta tìn thấy một cặp nào đó kề nhau và giống nhau
  length = up_to_index+1
  for j in range(1, length//2+1):
    # j là độ dài xét từ 1 đến 1 nửa độ dài chuỗi
    if (string[length-2*j:length-j] == string[length-j:length]):
      # Vì chứa chuỗi liền kề giống nhau nên không hợp lệ, trả về False
      return False
  # Tìm hết mà không có cái nào không hợp lệ thì trả về True
  return True


# Giải bài no-equal-adjancent substrings bằng backtracking
backtracker = BackTrackingSolver()
highest_value = 3
num_slots = 10
import time
t0 = time.time()
backtracker.solve(highest_value, checkSubstringsValid, num_slots, display=True)
solutions = backtracker.solutions
t1 = time.time()

for solution in solutions:
  print(solution)
print(len(solutions))
t2 = time.time()
# print("algorithm time = ", t1-t0)
# print("print time = ", t2-t1)