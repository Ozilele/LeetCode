// Best Time to Buy and Sell Stock III Problem
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int n = prices.length;
        // 2 tablice - maxProfitBeforeIndex, maxProfitAfterIndex
        int[] maxProfitBefore = new int[n];
        int[] maxProfitAfter = new int[n];
        int minPrice = prices[0];
        int maxPrice = prices[n - 1];
        maxProfitBefore[0] = 0;
        maxProfitAfter[n - 1] = 0;

        for(int i = 1; i < prices.length; i++) {
            if(prices[i] < minPrice) {
                minPrice = prices[i];
                maxProfitBefore[i] = maxProfitBefore[i - 1];
            } else if(prices[i] > minPrice) {
                if(prices[i] - minPrice > maxProfitBefore[i - 1]) {
                    maxProfitBefore[i] = prices[i] - minPrice;
                } else {
                    maxProfitBefore[i] = maxProfitBefore[i - 1];
                }
            } else {
                maxProfitBefore[i] = maxProfitBefore[i - 1];
            }
        }
        for(int k = n - 2; k >= 0; k--) {
            if(prices[k] < maxPrice) {
                if(maxPrice - prices[k] > maxProfitAfter[k + 1]) {
                    maxProfitAfter[k] = maxPrice - prices[k];
                } else {
                    maxProfitAfter[k] = maxProfitAfter[k + 1];
                }
            } else if(prices[k] > maxPrice) {
                maxPrice = prices[k];
                maxProfitAfter[k] = maxProfitAfter[k + 1];
            } else {
                maxProfitAfter[k] = maxProfitAfter[k + 1];
            }
        }
        for(int i = 0; i < prices.length; i++) {
            max = Math.max(maxProfitBefore[i] + maxProfitAfter[i], max);
        }
        return max;
    }
}
