class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        while (l < r, l != r):
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

        # #brute force
        # for i in range(len(numbers)):
        #   l = i
        #   r = len(numbers) - 1
        #   while( l < r and l != r):
        #     if numbers[l] + numbers[r] != target:
        #         r-=1
        #     else:
        #       return [l + 1, r + 1]
