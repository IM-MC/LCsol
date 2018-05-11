def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    prefix = ""

    if len(strs) == 0:
        return prefix

    w = strs[0]

    for i in range(len(w)):
        temp = prefix + w[i]
        for word in strs:
            if temp not in word[:i+1]:
                return prefix
        prefix += w[i]

    return prefix

print(longestCommonPrefix(["c", "acc", "ccc"]))
