# def quickSort(arr, start, end):
#   # stop condition
#   if start >= end:
#     return
#   # choose a pivot
#   print("quickSort for ", arr[start:end+1])
#   pivot = arr[end]
#   print("pivot = ", pivot)
#   # partition by pivot
#   tmp_idx = start
#   for idx in range(start, end):
#     if arr[idx] < pivot:
#       # swap value at idx with tmp_idx
#       arr[idx], arr[tmp_idx] = arr[tmp_idx], arr[idx]
#       tmp_idx += 1
#   print("left = ", arr[start: tmp_idx])
#   print("right = ", arr[tmp_idx: end])
#   # swap value at tmp_idx with end
#   arr[tmp_idx], arr[end] = arr[end], arr[tmp_idx]
#   print("return ", arr[start:end+1])
#   # devide to 2 list and call quickSort again
#   quickSort(arr, start = start, end = tmp_idx - 1)
#   quickSort(arr, start = tmp_idx + 1, end = end)

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

if __name__ == "__main__":
  arr = [9, -3, 5, 2, 6, 8, -6, 1, 3]
  reverse_quick(arr, start = 0, stop = len(arr) - 1)
  print("SORTED ARR = ", arr)