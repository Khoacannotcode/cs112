def mergeSort(arr):
  print("=====================================================")
  print("mergeSort arr = ", arr)
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    print("DEVIDE arr = {}   -->   L = {}, R = {}".format(arr, L, R))
    mergeSort(L)
    mergeSort(R)
    merge(arr, L, R)
  print("sorted : ", arr)
  

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


def conquerAndCombine(arr, L, R):
  print("conquerAndCombine({}, {}, {})".format(arr, L, R))
  i = j = k = 0
  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1
  while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1

if __name__ == "__main__":
  arr = [9,8,7,6,5,4,3,2,1]
  mergeSort(arr)
  print("=====================================================")
  print("SORTED ARRAY: ", arr)