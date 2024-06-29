array = [1, 3, 5, 5, 5, 5, 5, 5, 5, 7, 9, 11, 13, 13, 14]
target = 14

def bs(arr, k):
  low = 0
  high = len(arr) - 1
  
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == k:
      return mid
    elif arr[mid] > k:
      high = mid - 1
    else:
      low = mid + 1
  return -1

def bs_rec(arr, k, low, high):
  if low > high:
     return -1
  mid = (low + high) // 2
  if arr[mid] == k:
    return mid
  elif arr[mid] < k:
    return bs_rec(arr, k, mid + 1, high)
  else:
    return bs_rec(arr, k, low, mid - 1)
    
print(bs(array, target))
print(bs_rec(array, target, 0, len(array) - 1))