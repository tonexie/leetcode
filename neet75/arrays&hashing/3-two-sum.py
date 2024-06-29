from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashMap = {}

        # for i, n in enumerate(nums):
        #   value = hashMap.get(n, [])
        #   hashMap[n] = value.append(i)

        # for i, n in enumerate(nums):
        #   other = target - n
        #   if other in hashMap:
        #     if len(hashMap[other]) > 1 or hashMap[other][0] != i:
        #       return [i, hashMap[other][-1]]

        hashMap = {}

        for i, n in enumerate(nums):
          hashMap[n] = i

        for i, n in enumerate(nums):
          m = target - n
          if m in hashMap and hashMap[m] != i:
            return [i, hashMap[m]]

        l, r = 0, len(nums) - 1
        nums.sort()

        # while l < r:
        #     sum = nums[l] + nums[r]
        #     if sum == target:
        #         return [l, r]
        #     elif sum < target:
        #         l += 1
        #     else:
        #         r -= 1


nums = [3, 2, 3]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))
