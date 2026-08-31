class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_ptr = 0
        sell_ptr = None

        for i in range(1,len(prices)):
            if prices[buy_ptr] > prices[i]:
                buy_ptr = i
            elif prices[buy_ptr] < prices[i]:
                sell_ptr = i
            
            if sell_ptr != None:
                profit += prices[sell_ptr] - prices[buy_ptr]
                buy_ptr, sell_ptr = sell_ptr, None

        return profit