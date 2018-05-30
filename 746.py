def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """

    def countSteps(cost, memo, index):

        if index in memo:
            return memo[index]

        if index == len(cost)-1:
            memo[index] = cost[index]
            return memo[index]
        elif index > len(cost)-1:
            return 0

        for i in [1,2]:
            memo[index+i] = countSteps(cost, memo, index+i)

        memo[index] = min(memo[index+1], memo[index+2]) + cost[index]
        return memo[index]

    memo = {}
    ret = countSteps(cost, memo, 0)
    return min(memo[0],memo[1])

print(minCostClimbingStairs([3,6,12,3,41,5,61,100,34,21,23,40,5,2,681,23]))
