def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """

    product = [0] * (len(num1) + len(num2))
    pos = len(product) - 1

    res = ""

    for digita in reversed(num1):
        tempPos = pos
        for digitb in reversed(num2):
            tempProduct =  int(digita) * int(digitb)
            product[tempPos] += tempProduct
            product[tempPos-1] += product[tempPos]/10
            product[tempPos] = product[tempPos]%10
            tempPos -= 1
        pos -= 1

    first = 0
    while first < len(product)-1 and product[first] == 0:
        first += 1

    product = product[first:]

    for num in product:
        res += str(num)

    return res

print(multiply("123", "456"))
