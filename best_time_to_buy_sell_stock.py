'''
Problem Statement
You are given an array prices where prices[i] is the stock price on the i-th day.
Find the maximum profit you can achieve by buying on one day and selling on another day in the future.
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5  
# Buy at prices[1] = 1, Sell at prices[4] = 6 → Profit = 6 - 1 = 5

Example:
Input: prices = [7,6,4,3,1]
Output: 0  
# No profit can be made since prices keep decreasing.
'''

def max_profit(prices):
    min_price = float('inf')  # Start with a very high min price
    max_profit = 0  # Track the best profit

    for price in prices:
        if price < min_price:
            min_price = price  # Update min price
        else:
            max_profit = max(max_profit, price - min_price)  # Check profit

    return max_profit


prices = [7,1,5,3,6,4]
print(max_profit(prices))  # Output: 5

prices = [7,6,4,3,1]
print(max_profit(prices))  # Output: 0