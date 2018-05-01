def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    s = list(s)
    vowels = "aeiouAEIOU"

    index = []

    for i in range(len(s)):
        if s[i] in vowels:
            index.append(i)

    print(index)
    if len(index) >= 2:
        for i in range(len(index)/2):
            right = len(index) - 1 - i
            sub = s[index[i]]
            s[index[i]] = s[index[right]]
            s[index[right]] = sub

    return "".join(s)

print(reverseVowels("aA"))
