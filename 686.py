def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """

    count = 1
    length = len(A)
    copyA = A
    while (len(copyA) < len(B)):
        count += 1
        copyA += A

    if len(copyA) >= len(B) and B not in copyA:
        count += 1
        copyA += A

    return count if B in copyA else -1

print(repeatedStringMatch("a", "aa"))
