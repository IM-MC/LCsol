def getPermutation( n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """

    res, nums = "",  range(1, n+1)
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res
