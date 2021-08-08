# num_test_case = int(input())
# for this_test_case in range(num_test_case):
#   in_str = input()
#   m = int(in_str.split(" ")[0])
#   n = int(in_str.split(" ")[1])
#   k = int(in_str.split(" ")[2])
#   arr1 = input().split(" ")
#   arr1 = [int(x) for x in arr1]
#   arr2 = input().split(" ")
#   arr2 = [int(x) for x in arr2]
#   arr = arr1 + arr2
#   quickSrt(arr, start=0, stop=m+n-1)
#   out_list.append(arr[k])

def quickSrt(arr, start, stop):
  if start >= stop:
    return
  # define pivot and tmp_idx
  pivot = arr[stop]
  tmp_idx = start
  for idx in range(start, stop):
    if arr[idx] < pivot:
      #swap idx <--> tmp_idx
      arr[idx], arr[tmp_idx] = arr[tmp_idx], arr[idx]
      tmp_idx += 1
  # swap tmp_idx <--> stop
  arr[tmp_idx], arr[stop] = arr[stop], arr[tmp_idx]
  # call recurrent
  quickSrt(arr, start = start, stop = tmp_idx - 1)
  quickSrt(arr, start = tmp_idx + 1, stop = stop)
out_str = ""
input_str = input()
input_list = input_str.split('\n')[1:]
for idx in range(0, len(input_list), 3):
  in_str = input_list[idx]
  if in_str == '':
    break
  m = int(in_str.split(" ")[0])
  n = int(in_str.split(" ")[1])
  k = int(in_str.split(" ")[2])
  arr1 = input_list[idx+1].split(" ")
  arr1 = [int(x) for x in arr1]
  arr2 = input_list[idx+2].split(" ")
  arr2 = [int(x) for x in arr2]
  arr = arr1 + arr2
  quickSrt(arr, start=0, stop=m+n-1)
  out_str = out_str + str(arr[k]) + "\n"

print(out_str)