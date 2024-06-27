# array = [1, 3, 5, 5, 5, 5, 5, 5, 5, 7, 9, 11, 13]
# target = 7

# # iterative
# def binary_search(array, target):
  
# # recursive
# def binary_search_rec(array, target, low, high):


# print(f"Target {target} found at index {result1} and {result2}.")

array = [1, 3, 5, 5, 5, 5, 5, 5, 5, 7, 9, 11, 13]
target = 7

# iterative
def binary_search(array, target):
  low = 0
  high = len(array) - 1
  
  while low <= high:
    mid = (low + high) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
      
  return -1
  
# recursive
def binary_search_rec(array, target, low, high):
  if low > high:
    return -1
  mid = (low + high) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search_rec(array, target, low, mid - 1)
  else:
    return binary_search_rec(array, target, mid + 1, high)
  

result1 = binary_search(array, target)
result2 = binary_search_rec(array, target, 0, len(array) - 1)

print(f"Target {target} found at index {result1} and {result2}.")
