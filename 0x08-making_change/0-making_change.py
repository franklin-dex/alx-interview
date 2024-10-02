#!/usr/bin/python3

'''
Making changes
'''


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be made with the coins.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it's not possible.
    """

    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
