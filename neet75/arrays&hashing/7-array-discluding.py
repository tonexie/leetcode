from typing import List
from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrL, arrR, res = [1], [1], []
        currL, currR = 1, 1
        for i in range(len(nums) - 1):
          currL *= nums[i]
          arrL.append(currL)
          
        for i in range(len(nums) - 1, 0, -1):
          currR *= nums[i]
          arrR.append(currR)
        arrR.reverse()

        for i in range(len(arrL)):
          res.append(arrL[i] * arrR[i])
          
        return res

nums = [1,2,4,6]
sol = Solution()
print(sol.productExceptSelf(nums))
        