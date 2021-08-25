# Framework cho backtracking
class BackTrackingSolver():
  def __init__(self):
    self.solutions = set()
  def solve(self,values, safe_up_to, size, display=False):
    """Tìm solution cho bài toán dạng backtracking

    values      -- Một chuỗi các giá trị cần thử một cách lần lượt
                -- Ví dụ bài map-coloring-problem thì có thể values = ['red', 'green', 'blue']
    
    safe_up_to  -- Một FUNCTION với 2 args: solution và position. Hàm này cũng có thể gọi là hàm CHECKER
                -- Trong đó solution là các value từ 0 -> position
                -- Chúng ta cần check xem solution này có valid hay không.

    size        -- Số lượng "slot" mà chúng ta muốn fill
                -- Trong bài 8-queen thì ta cần điền 8 slot cho 8 quân Hậu. Tăng số hậu thì tăng slot
                -- Trong bài no-equal-adjancent substrings thì ta cần gen chuỗi dài bao nhiêu thì slot bấy nhiêu.
                --- Trong bài sudoku thì slot phụ thuộc vào việc board to bao nhiêu
    """
    solution = [None] * size

    def extend_solution(position):
      """append 1 step to solution at position"""
      for value in values:
        solution[position] = value
        if display:
          print("-".join(str(x) for x in solution))
        if safe_up_to(solution, position):
        # aka if check_valid(solution, position) is True
          if position >= size-1 or extend_solution(position+1):
          # Không hiểu dòng if này
            self.solutions.add("".join(str(x) for x in solution))
            # return "".join(str(x) for x in solution)
            # return solution
      return None
    
    return extend_solution(0)

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
values = [0,1,2]
size = 10
backtracker.solve(values, checkSubstringsValid, size, display=False)
solutions = backtracker.solutions

for solution in solutions:
  print(solution)
print(len(solutions))