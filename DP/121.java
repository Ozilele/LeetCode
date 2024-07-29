// Best Time to Buy and Sell Stock Problem
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution {

    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int l = 0; // buy price
        int r = 1; // sell price
        while(r < prices.length) {
            if(prices[l] >= prices[r]) {
                l = r;
                r++;
            } else {
                int curr_max = prices[r] - prices[l];
                if(curr_max > max_profit) {
                    max_profit = curr_max;
                }
                r++;
            }
        }
        return max_profit;
    }
}