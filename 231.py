def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n > 1:
      while n%2 == 0:
        n /= 2

    return n == 1
