from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        l, r = 0, 0

        for r, price in enumerate(prices):
            if price < minPrice:
                l = r
                minPrice = price
            if l != r:
                maxProfit = max(maxProfit, prices[r] - prices[l])
        return maxProfit

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))
