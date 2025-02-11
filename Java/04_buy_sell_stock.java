
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;

        int l = 0;
        int r = 1;

        while (r < prices.length) {
            int currentProfit = prices[r] - prices[l];
            if (currentProfit > 0) {
                maxProfit = Math.max(currentProfit, maxProfit);
            } else {
                l = r;
            }
            r++;
        }

        return maxProfit;
    }
}