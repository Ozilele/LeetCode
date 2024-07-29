# Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

class Solution:
    def maxProfit(self, k: int, prices) -> int:
        n = len(prices)
        profits = [[0] * (k + 1) for _ in range(n)]

        # max_diff przechowuje różnicę maksymalną zysków, którą można uzyskać do dnia i-1 przy 
        # x−1 transakcjach minus cena akcji w dniu i.
        for x in range(1, k + 1): # iteracja po liczbie transakcji
            price_diff = -prices[0]
            for i in range(1, n): # iteracja po liczbie dni majac danego x - liczbe mozliwych transakcji
                profits[i][x] = max(profits[i - 1][x], prices[i] + price_diff) # dla danego dnia poprzedni profit, lub sell 
                price_diff = max(price_diff, profits[i-1][x-1] - prices[i])
        return profits[n-1][k]
