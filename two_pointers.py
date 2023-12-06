'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
'''

def max_profit(prices):
    # accumulator variable to track profit
    profit = 0
    # track two pointers, today and tomorrow
    today = 0
    tomorrow = 1
    # loop through prices, comparing today's price to tomorrow's
    while tomorrow < len(prices):
        # if tomorrow's price > today's, add the difference to the profit
        trade_value = prices[tomorrow] - prices[today]
        if trade_value > 0:
            # if tomorrow's price > today's, add the difference to the profit
            profit += trade_value
        # increment the days
        today += 1
        tomorrow += 1

    return profit