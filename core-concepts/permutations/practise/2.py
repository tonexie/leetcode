from collections import deque

def permutations(nums):
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

print(permutations([1,2,3]))