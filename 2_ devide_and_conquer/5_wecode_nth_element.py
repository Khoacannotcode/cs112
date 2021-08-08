in_str = input()
n,k = int(in_str.split(" ")[0]), int(in_str.split(" ")[1])
input_list = []
for count in range(n):
  input_list.append(int(input()))
  
def reverse_quick(arr, start, stop):
  if start >= stop:
    return
  # define pivot and tmp_idx
  pivot = arr[stop]
  tmp_idx = start
  for idx in range(start, stop):
    if arr[idx] > pivot:
      #swap idx <--> tmp_idx
      arr[idx], arr[tmp_idx] = arr[tmp_idx], arr[idx]
      tmp_idx += 1
  # swap tmp_idx <--> stop
  arr[tmp_idx], arr[stop] = arr[stop], arr[tmp_idx]
  # call recurrent
  reverse_quick(arr, start = start, stop = tmp_idx - 1)
  reverse_quick(arr, start = tmp_idx + 1, stop = stop)

reverse_quick(input_list, start=0, stop=len(input_list)-1)
print(input_list[k-1])