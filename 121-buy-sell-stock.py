class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_price = 0
        
        # for i in range(len(prices)):
        #   for j in range(i, len(prices)):
        #     if prices[j] - prices[i] > max_price:
        #       max_price = prices[j] - prices[i]
        
        # return max_price
        
        profit = 0
        cheapest = prices[0]
        
        for price in prices:
          if price < cheapest:
            cheapest = price
          temp = price - cheapest
          if temp > profit:
            profit = temp
          
        return profit
          