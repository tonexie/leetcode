from collections import deque

def permutate(nums):
  res = []
  queue = deque([[]])
  
  while queue:
    currQ = queue.popleft()
    if len(currQ) == len(nums):
      res.append(currQ)
      
    for n in nums:
      if n not in currQ:
        sub = currQ + [n]
        queue.append(sub)
        
  return res

print(permutate([1,2,3]))