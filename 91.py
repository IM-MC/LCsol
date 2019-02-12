def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    n = len(s)

    if n == 0:
        return 0

    memo = [0]*(n+1)
    memo[n] = 1
    memo[n-1] = 1 if s[n-1] != '0' else 0

    for i in range(n-2,-1,-1):
        if s[i] == '0':
            continue

        memo[i] = memo[i+1]+memo[i+2] if int(s[i:i+2]) <= 26 else memo[i+1]

    return memo[0]


print(numDecodings("29483325"))
