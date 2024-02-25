class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() 
        output = []
        
        for i, num in enumerate(nums):
            if nums[i - 1] == nums[i] and i > 0:
                continue
            target = -num
            l, r = i + 1, len(nums) - 1
            while l < r and l != r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] == target:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l != r:
                        l += 1
        return output
    
solution = Solution()
nums = [0,0,0]
print(solution.threeSum(nums))