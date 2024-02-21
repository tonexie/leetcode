class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotated_array = []
        if (k > len(nums)):
          k = k % len(nums)
        for i in range(len(nums) - k, len(nums)):
          rotated_array.append(nums[i])
        for i in range(len(nums) - k):
          rotated_array.append(nums[i])
          
        nums[:] = rotated_array
        
nums = [-1, -2]
k = 6
        
solution = Solution()
solution.rotate(nums, k)
print(nums)