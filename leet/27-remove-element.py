class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        originalLen = len(nums)
        
        while val in nums:
            nums.remove(val)
        
        return len(nums)
    
nums = [0,1,2,2,3,0,4,2]
val = 2

solution = Solution()
print(solution.removeElement(nums, val))
print(nums)

