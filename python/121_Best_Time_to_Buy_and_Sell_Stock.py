# When doing greedy method. One important thing to keep in mind is what variable
# will be required to store. Here we need to now what the current best
# profit is and what is the lowest buy-in time.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            # Check if we have a new maximum profit
            max_profit = max(max_profit, prices[i] - min_price)
            # Potentially find a new lowest buy-in point.
            min_price = min(min_price, prices[i])

        return max_profit

# ------------------------------------------------------------------------------
# Second solution is Kadane's Algorithm. We have an array to store the difference
# between two consecutive days.
# One important thing is to reset current_profit back to 0 when it is lower than 0.
# This is because once we reach this point, we actually found a new lowest buy-in
# time. So we should start from here.
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        price_difference = [0] * len(prices)
        price_difference[0] = 0
        for i in range(1, len(prices)):
            price_difference[i] = prices[i] - prices[i-1]

        maximum_profit = 0
        current_profit = 0
        for i in range(len(prices)):
            current_profit += price_difference[i]
            if current_profit < 0:
                current_profit = 0
            maximum_profit = max(maximum_profit, current_profit)

        return maximum_profit
