from collections import deque


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # key insight is to use pre for one before, and post for one after
        pre = deque()
        post = deque()
        output = []

        preNum = 1
        postNum = 1

        for num in nums:
            preNum = preNum * num
            pre.append(preNum)

        for i in range(len(nums) - 1, -1, -1):
            postNum = postNum * nums[i]
            post.appendleft(postNum)

        for i in range(len(nums)):
            if i == 0:
                output.append(post[i + 1])
            elif i == len(nums) - 1:
                output.append(pre[i - 1])
            else:
                output.append(pre[i - 1] * post[i + 1])

        return output

# neet
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [1] * len(nums)
        
        # creates a array where each index shows the product of numbers before
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res


solution = Solution()
nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))
