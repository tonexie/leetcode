class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []

        # top loop fixes the left most element
        for i, num in enumerate(nums):
            # check for duplicates
            if nums[i - 1] == nums[i] and i > 0:
                continue
            target = -num
            # two sum here, but continued
            l, r = i + 1, len(nums) - 1
            while l < r and l != r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] == target:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # check for duplictes here again
                    while nums[l - 1] == nums[l] and l != r:
                        l += 1
        return output


solution = Solution()
nums = [0, 0, 0]
print(solution.threeSum(nums))
