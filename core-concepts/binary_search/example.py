array = [1, 3, 5, 7, 9, 11, 13]
target = 7


# iterative
def binary_search(array, target):
  pass
# recursive
def binary_search_rec(array, target, low, high):
  pass
result1 = binary_search(array, target)
result2 = binary_search_rec(array, target)

print(f"Target {target} found at index {result1} and {result2}.")
  

# iterative
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid  # Target found
        elif array[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Target not found

# Example usage
array = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(array, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")

# recursive
def binary_search_rec(array, target, low, high):
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2

    if array[mid] == target:
        return mid  # Target found
    elif array[mid] < target:
        return binary_search_rec(array, target, mid + 1, high)  # Search in the right half
    else:
        return binary_search_rec(array, target, low, mid - 1)  # Search in the left half

# Example usage
array = [1, 3, 5, 7, 9, 11, 13]
target = 7

# Initial call to the function with the entire range of the array
result = binary_search_rec(array, target, 0, len(array) - 1)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")
