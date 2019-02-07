def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    dic = dict()
    res = []

    for i in range(len(strs)):
        checker = [0]*26
        for char in strs[i]:
            value = ord(char) - ord('a')
            checker[value] += 1

        key = tuple(checker)
        if key not in dic.keys():
            dic[key] = [strs[i]]
        else:
            dic[key].append(strs[i])

    for key in dic.keys():
        res.append(dic[key])

    return res

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
