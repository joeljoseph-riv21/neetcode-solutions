class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        TAKEAWAYS:
        - Evaluates the chances for profit per day: It looks at each day compared to the previous day.
        doesn't tell you when to sell or buy.
        - Calculates the total maximum profit from multiple transactions: It assumes you can perform as many 
        transactions as you want.
        - If the price goes up from day X to day Y, it assumes you would have bought on day X and sold on day Y,
        and adds that immediate profit to the total.
        """

        if not prices or len(prices)<2:
           return False

        maximum_profit = 0

        for amount in range(1, len(prices)):
            if prices[amount] >  prices[amount - 1]: # comparing today with yesterday's price
               maximum_profit =  maximum_profit + prices[amount] - prices[amount - 1] # implies SP on today - CP from yesterday + current profit
        return maximum_profit 
                     