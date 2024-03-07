import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxQ = collections.deque()
        output = []
        
        # Function to clean the deque from elements outside the current window
        def clean_deque(index):
            if maxQ and maxQ[0] == index - k:
                maxQ.popleft()
        
        # Initial filling of maxQ and output
        for i in range(k):
            clean_deque(i)
            while maxQ and nums[i] >= nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
        output.append(nums[maxQ[0]])
        
        # Sliding the window and updating maxQ and output
        for i in range(k, len(nums)):
            clean_deque(i)
            while maxQ and nums[i] >= nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
            output.append(nums[maxQ[0]])
        
        return output

sol = Solution()
nums = [1, -1]
k = 1
print(sol.maxSlidingWindow(nums, k))
