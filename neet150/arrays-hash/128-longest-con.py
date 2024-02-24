class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numHash = {}

        for num in nums:
            numHash[num] = False

        longestStreak = 0
        for n in numHash:
            if numHash[n]:  # check if number has been read
                continue

            numHash[n] = 1
            count = 1
            up = n
            low = n
            while True:
                if up + 1 in numHash:
                    up += 1
                    numHash[up] = True
                    count += 1
                elif low - 1 in numHash:
                    low -= 1
                    numHash[low] = True
                    count += 1
                else:
                    if count > longestStreak:
                        longestStreak = count
                    break

        return longestStreak
      
# neet
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


solution = Solution()
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(solution.longestConsecutive(nums))
