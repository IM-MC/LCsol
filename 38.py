def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """

    s = '1'
    for _ in range(n-1):
        temp = ""
        count = 0
        check = s[0]
        print(s)
        for char in s:
            if char == check:
                count += 1
            else:
                temp += str(count) + check
                count = 1
                check = char

        temp += str(count) + check
        s = temp

    return s

print(countAndSay(6))
