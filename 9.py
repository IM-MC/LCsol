def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    number = str(x)

    if number[::-1] != number:
        return False
    else:
        return True

print(isPalindrome(123321))
