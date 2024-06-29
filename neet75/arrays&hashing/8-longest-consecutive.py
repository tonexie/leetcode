from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        countSet = set()
        highest = 0
        for n in nums:
          countSet.add(n)
        
        for key in countSet:
          count = 0
          if key - 1 in countSet:
            count = 1
          else:
            next = key
            while next in countSet:
              count += 1
              next += 1
          highest = max(highest, count)
        
        return highest

nums = [0,3,2,5,4,6,1,1]
sol = Solution()
print(sol.longestConsecutive(nums))
            
              
          