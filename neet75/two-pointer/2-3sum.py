from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == -num:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum < -num:
                    l += 1
                else:
                    r -= 1
                

        return res


nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
sol = Solution()
print(sol.threeSum(nums))
