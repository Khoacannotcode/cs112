def findInversionCount_BruteForce(arr):
  invertsion_count = 0 
  for idx1 in range(len(arr)-1):
    for idx2 in range(idx1 + 1, len(arr)):
      if (arr[idx1] > arr[idx2]):
        invertsion_count += 1
  return invertsion_count

# def findInversionCount_BruteForce(arr):


import random
import time
if __name__ == '__main__':
  arr = random.sample(range(10, 30), 10e9)
  arr1 = arr.copy()
  arr2 = arr.copy()
  t1 = time.time()
  print("Brute Force Inversion count is", findInversionCount_BruteForce(arr1))
  t2 = time.time()
  print("Brute Force time execution: ", t2 - t1)
