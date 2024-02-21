class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dictionary keys must be unique
        
        nums_dict = {}
        for num in nums:
          nums_dict[num] = "hi"
        
        nums[:] = nums_dict.keys()
        nums.sort()
        return len(nums)
      
nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
print(solution.removeDuplicates(nums))