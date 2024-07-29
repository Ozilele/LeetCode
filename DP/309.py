# Best Time to Buy and Sell Stock with Cooldown Problem
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        s0 = [0] * n
        s1 = [0] * n
        s2 = [0] * n
        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = 0
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = prices[i] + s1[i-1]
        return max(s0[n-1], s2[n-1])

    # P(i) - max profit sprzedając akcje i-tego dnia
    # P(i) = max{prices[i] - prices[j], P(k) + (prices[i] - min{prices[z]})}
    def profit(self, prices) -> int:
        n = len(prices)
        profits = [0] * n 
        for i in range(1, n):
            maxProfit = 0
            maxPrev = 0
            for j in range(i):
                if(prices[i] - prices[j] > maxProfit):
                    maxProfit = max(prices[i] - prices[j], maxProfit)    
                if(i-3 >= 0 and j <= i-3):
                    min_buy = 100000
                    for k in range(j+2, i): # k+2 <= z <= i-1
                        min_buy = min(prices[k], min_buy)
                    maxPrev = profits[j] + (prices[i] - min_buy)
            maxProfit = max(maxProfit, maxPrev)
            profits[i] = maxProfit
        maxik = 0
        for i in range(n):
            maxik = max(maxik, profits[i])
        return maxik