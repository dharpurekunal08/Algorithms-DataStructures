# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')  # Initialize min price to positive infinity

        for price in prices:
            min_price = min(min_price, price)  # Update min price if current price is lower
            max_profit = max(max_profit, price - min_price)  # Calculate potential profit based on min price

        return max_profit