// Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution {

    public int maxProfit(int[] prices) {
        int max = 0;
        int i = 0;
        int buy_ind = i;
        int sell_ind = i + 1;
        int currPrice = prices[0];

        for(int k = i + 1; k < prices.length; k++) {
            // if(prices[k - 1] > prices[k]) {
            //     buy_ind = k;
            //     sell_ind = k + 1;
            // }
            if(prices[k] > currPrice) {
                max += prices[k] - currPrice;
            }
            currPrice = prices[k];
        }
        return max;
    }
}

