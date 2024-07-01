from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] > nums[r]:
              l = mid + 1
            else:
              r = mid
        
        return nums[r]

nums = [3,4,5,1,2]
sol = Solution()
print(sol.findMin(nums))
        
            
