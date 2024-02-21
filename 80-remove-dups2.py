class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 2
        for i in (range(2, len(nums))):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j
        
        # i = 0
        # for n in nums:
        #     if i < 2 or n > nums[i-2]:
        #         nums[i] = n
        #         i += 1
        # return i

                
                    
    
nums = [1,1,1,2,2,3]

solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)