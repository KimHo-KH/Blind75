from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit