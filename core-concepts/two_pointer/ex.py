# Given an array of integers and a target sum, 
# find all unique pairs of integers in the array that sum up to the target.

nums = [1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

def two_sum(nums, k):
  nums.sort()
  l, r = 0, len(nums) - 1
  res = []
  
  while l < r:
    currSum = nums[l] + nums [r]
    if currSum == k:
      res.append((nums[l], nums[r]))
      l += 1
      while l < r and nums[l] == nums[l - 1]:
        l += 1
    elif currSum < k:
      l += 1
    else:
      r -= 1
  
  return res

print(two_sum(nums, target))