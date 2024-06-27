from collections import deque

def subsets(nums):
  result = []
  queue = deque([[]])
  
  while queue:
    currQ = queue.popleft() # kinda lke my node
    result.append(currQ)
    for n in nums:
      if not currQ or n > currQ[-1]:
        sub = currQ + [n]
        queue.append(sub)
  
  return result

print(subsets([1,2,3]))