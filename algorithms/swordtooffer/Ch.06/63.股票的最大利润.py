def maxprofit(prices):
    buy = float('inf')
    profit = 0
    for i in prices:
        if i < buy:
            buy = i
        else:
            if i - buy > profit:
                profit = i - buy
    return profit
