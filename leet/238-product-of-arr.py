class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        ans = [1] * n
        cur = 1
        for i in range(n):
          ans[i] = cur
          cur *= nums[i]
          
        cur = 1
        for i in range(n):
          ans[n - i - 1] *= cur
          cur *= nums[n - i - 1]
          
        return ans
      
test = [1,2,3,4]   
solution = Solution()
solution.productExceptSelf(test)