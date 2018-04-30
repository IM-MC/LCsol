def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """

    if n > 1:
        while n%3 == 0:
            n /= 3

    return n == 1

print(isPowerOfThree(45))
