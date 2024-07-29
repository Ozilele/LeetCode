# Coin Change Problem
# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        max = amount + 1
        dp = [max] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(0, n):
                if(coins[j] <= i):
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]