from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = set()
        for num in nums:
            if num not in existing:
                existing.add(num)
            else:
              return True
        return False

nums = [1, 2, 3, 3]
sol = Solution()
print(sol.hasDuplicate(nums))