def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    merge(arr, L, R)
  return

def merge(arr, L, R):
  idx_L = idx_R = idx_arr = 0
  while idx_L < len(L) and idx_R < len(R):
    if L[idx_L] < R[idx_R]:
      arr[idx_arr] = L[idx_L]
      idx_L += 1
    else:
      arr[idx_arr] = R[idx_R]
      idx_R += 1
    idx_arr += 1
  while idx_L < len(L):
    arr[idx_arr] = L[idx_L]
    idx_L += 1
    idx_arr += 1
  while idx_R < len(R):
    arr[idx_arr] = R[idx_R]
    idx_R += 1
    idx_arr += 1



# def quickSort(arr, start, end):
#   # stop condition
#   if start >= end:
#     return
#   # choose a pivot
#   pivot = arr[end]
#   # partition by pivot
#   tmp_idx = start
#   for idx in range(start, end):
#     if arr[idx] < pivot:
#       # swap value at idx with tmp_idx
#       arr[idx], arr[tmp_idx] = arr[tmp_idx], arr[idx]
#       tmp_idx += 1
#   # swap value at tmp_idx with end
#   arr[tmp_idx], arr[end] = arr[end], arr[tmp_idx]
#   # devide to 2 list and call quickSort again
#   quickSort(arr, start = start, end = tmp_idx - 1)
#   quickSort(arr, start = tmp_idx + 1, end = end)

def quickSort(arr, start, stop):
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
  quickSort(arr, start = start, stop = tmp_idx - 1)
  quickSort(arr, start = tmp_idx + 1, stop = stop)

import random
import time
if __name__ == '__main__':
  limit = int(10e1) 
  print("limit = ", limit)
  arr = random.sample(range(-limit, limit), limit)
  arr1 = arr.copy()
  arr2 = arr.copy()
  t1 = time.time()
  mergeSort(arr1)
  print(arr1)
  t2 = time.time()
  quickSort(arr2, start = 0, stop = len(arr2) - 1)
  print(arr2)
  t3 = time.time()
  print("mergeSort takes ", t2 - t1)
  print("quickSort takes ", t3 - t2)
