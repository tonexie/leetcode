class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # max_no = len(nums) / 2
        
        # for i in range(len(nums)):
        #   count = 0
        #   for j in range(i, len(nums)):
        #     if nums[i] == nums[j]:
        #       count += 1
        #     if count > max_no:
        #       return nums[i]
        
        nums.sort()
        return nums[(len(nums) // 2)]
      
      
        # n = len(nums)
        #   m = defaultdict(int) // initializes a default empty value, which in this case is zero for int
          
        #   for num in nums:
        #       m[num] += 1
          
        #   n = n // 2
        #   for key, value in m.items():
        #       if value > n:
        #           return key
          
        #   return 0
      
solution = Solution()
nums = [2,2,1,1,1,2,2]
print(solution.majorityElement(nums))