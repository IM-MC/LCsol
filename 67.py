def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    diff = len(a) - len(b)
    sum = [0] * (max(len(a),len(b)) + 1)
    pos = len(sum)-1

    if diff < 0:
        a = "0"*(diff*-1) + a
    elif diff > 0:
        b = "0"*(diff) + b

    for i in range(len(a)-1, -1, -1):
        tempPos = pos
        sum[tempPos] += int(a[i]) + int(b[i])
        sum[tempPos-1] += sum[tempPos]/2
        sum[tempPos] %= 2
        print(sum)
        pos -= 1

    start = 0
    while start < len(sum)-1 and sum[start] == 0:
        print(start)
        start += 1

    return ''.join(map(str,sum[start:]))

print(addBinary("1010", "1011"))
