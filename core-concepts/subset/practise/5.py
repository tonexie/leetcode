from collections import deque

def subsets(nums):
  queue = deque([[]])
  res = []
  
  while queue:
    currQ = queue.popleft()
    res.append(currQ)
    for n in nums:
      if not currQ or n > currQ[-1]:
        sub = currQ + [n]
        queue.append(sub)
        
  return res

print(subsets([1,2,3,4]))