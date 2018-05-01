def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """


    left = 1
    right = n

    while left < right:
        mid = left + (right-left)/2
        if guess(mid) == 1:
            left = mid + 1
        else:
            right = mid

    return left
