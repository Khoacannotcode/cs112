tmp_str = "5\n8 1 6\n0 0 2 3 3 3 5 6\n0\n2 3 3\n1 1\n1 3 3\n8 8 14\n2 4 4 6 7 7 7 7\n0 0 1 3 3 4 4 5\n6 9 7\n1 1 3 3 3 3\n1 2 2 4 6 7 9 9 9\n9 8 3\n0 2 3 4 6 8 8 10 12\n2 4 6 6 7 8 8 9\n"
tmp_str2 = "5\n9 7 4\n2 2 2 4 6 8 9 11 12\n1 1 1 2 2 3 3\n1 1 1\n2\n0\n1 8 3\n0\n0 1 3 5 7 9 10 11\n1 5 0\n0\n0 1 2 3 5\n6 3 2\n0 1 1 1 2 2\n2 3 4\n"
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


# out_list = []
# input_list = tmp_str2.split("\n")[1:]
# for idx in range(0, len(input_list), 3):
#   in_str = input_list[idx]
#   if in_str == '':
#     break
#   m = int(in_str.split(" ")[0])
#   n = int(in_str.split(" ")[1])
#   k = int(in_str.split(" ")[2])
#   arr1 = input_list[idx+1].split(" ")
#   arr1 = [int(x) for x in arr1]
#   arr2 = input_list[idx+2].split(" ")
#   arr2 = [int(x) for x in arr2]
#   arr = arr1 + arr2
#   quickSrt(arr, start=0, stop=m+n-1)
#   out_list.append(arr[k])

# for item in out_list:
#   print(item)

out_str = ""
# input_str = input()
input_list = tmp_str2.split('\n')[1:]
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