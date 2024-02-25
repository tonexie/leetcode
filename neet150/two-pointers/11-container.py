class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height) - 1

        maxVol = (r - l) * min(height[l], height[r])

        while l < r:
            # only increment the pointer that has the smallest height
            if height[l] < height[r]:
                switch = True
            else:
                switch = False

            if switch:
                # ensure incremented height is taller than original height
                currH = height[l]
                l += 1
                while height[l] < currH and l < r:
                    l += 1
            else:
                currH = height[r]
                r -= 1
                while height[r] < currH and l < r:
                    r -= 1

            maxVol = max(maxVol, (r - l) * min(height[l], height[r]))

        return maxVol


solution = Solution()
height = [2, 3, 4, 5, 18, 17, 6]
print(solution.maxArea(height))
