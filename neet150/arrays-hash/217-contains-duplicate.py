# my solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        newList = set()
        for i in range(len(nums)):
            newList.add(nums[i])
        
        if len(newList) < len(nums):
            return True
        return False

# neet solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

solution = Solution()
nums = [1,2,3,4]
print(solution.containsDuplicate(nums))