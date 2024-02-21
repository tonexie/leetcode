class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy = 0
        # current_max = 0
        # profit = 0
        
        # for day in range(1, len(prices)):
        #   if prices[day] >= prices[buy]:
        #     temp_max = prices[day] - prices[buy]
        #     if temp_max > current_max:
        #       current_max = temp_max
        #     else:
        #       buy = day
        #       profit += current_max
        #       current_max = 0
        #   else:
        #     buy = day
        #     profit += current_max
        #     current_max = 0
        
        # profit += current_max 
        # return profit
        
        profit = 0
        
        for day in range(1, len(prices)):
          if prices[day] > prices[day - 1]:
            profit += prices[day] - prices[day - 1]
        
        return profit
      

prices = [2,1,2,0,1]
solution = Solution()
print(solution.maxProfit(prices))