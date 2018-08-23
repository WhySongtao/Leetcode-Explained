/*
# When doing greedy method. One important thing to keep in mind is what variable
# will be required to store. Here we need to now what the current best
# profit is and what is the lowest buy-in time.
*/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length === 0 || prices.length === 1) {
        return 0;
    }

    let min_price = prices[0];
    let max_profit = 0;

    for(let i = 1; i < prices.length; i++){
        max_profit = Math.max(max_profit, prices[i] - min_price);
        min_price = Math.min(min_price, prices[i]);
    }

    return max_profit;
};
