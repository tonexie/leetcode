from typing import List
from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      
      def dfs():
        stack = deque([candidates[0]])
        idx = 0
        while stack:
          curr = stack.pop()
          sum = 0
          for n in curr:
            sum += n
          if sum == target:
            res.append(curr)
          elif sum < target:
            stack.append([curr] + [candidates[idx]])
          else:
            stack.pop()
            idx += 1
            if (idx < len(candidates)):
              stack.append([curr])