class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices)<2:
           return False

        maximum_profit = 0

        for amount in range(1, len(prices)):
            if prices[amount] >  prices[amount - 1]:
               maximum_profit =  maximum_profit + prices[amount] - prices[amount - 1] 
        return maximum_profit
                     
                 

               

        

        