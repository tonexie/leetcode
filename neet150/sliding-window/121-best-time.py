class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        maxPrice = 0
        
        for price in prices:
            if price < min:
                min = price
            maxPrice = max(maxPrice, price - min)

        return maxPrice

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        lMin = prices[l]
        if len(prices) > 1:
          rMax = prices[r]
        else:
          rMax = 0
        maxPrice = rMax - lMin

        for i in range(len(prices) - 1):
            r = i + 1
            l = i    
            if prices[l] < lMin:
                lMin = prices[l]
            maxPrice = max(maxPrice, prices[r] - lMin)

        return max(0, maxPrice)
      
solution = Solution()
prices= [7,1,5,3,6,4]
print(solution.maxProfit(prices))
