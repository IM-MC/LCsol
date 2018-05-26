def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    def countSteps(n, memo):

        if memo == None:
            memo = {2:2,
                    1:1}

        if n in memo:
            return memo[n]

        for i in [1,2]:
            memo[n-i] = countSteps(n-i, memo)

        memo[n] = memo[n-1] + memo[n-2]
        return memo[n]

    ret = countSteps(n, None)
    return ret

print(climbStairs(5))
