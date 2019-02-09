def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1

    if n < 0:
        x = 1/x
        n = -n

    ans = 1
    while n:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1

    return ans 

print(myPow(2,4))
