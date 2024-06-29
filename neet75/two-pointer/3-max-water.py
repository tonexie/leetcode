from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea


heights = [1, 7, 2, 5, 4, 7, 3, 6]
sol = Solution()
print(sol.maxArea(heights))
