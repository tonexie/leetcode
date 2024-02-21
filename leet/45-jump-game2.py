class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        node_end = 0
        furthest = 0
        
        for i in range(len(nums) - 1):
          furthest = max(furthest, nums[i] + i)
          if furthest >= len(nums) - 1:
            steps += 1
            break
          if i == node_end:
            node_end = furthest
            steps += 1
        
        return steps
