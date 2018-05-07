def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    result = 0
    neg = False

    if x < 0:
        neg = True
        x *= -1

    while x != 0 and x != -1:
        digit = x%10
        new = (result*10) + digit
        if (abs(new) > (2**31 -1)):
            return 0
        result = new
        x = x/10

    if neg:
        result *= -1

    return result

print(reverse(1534236469))
