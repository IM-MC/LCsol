def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if len(prices) == 0:
        return 0

    min, profit = prices[0] ,0

    for day in range(1, len(prices)):
        if prices[day] < min:
            min = prices[day]
        else:
            temp = prices[day] - min
            if temp > profit:
                profit = temp

    return profit

print(maxProfit([7,1,5,3,6,4]))
