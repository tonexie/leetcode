class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current_end = len(nums) - 1
        jumpable = False
        
        for i in range(len(nums) - 1, -1, -1):
          if i + nums[i] >= current_end:
            current_end = i
            jumpable = True
          else:
            jumpable = False
            
        return jumpable
      
      
nums = [2,3,1,1,4]

solution = Solution()
solution.canJump(nums)