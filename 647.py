def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """

    count = [0]

    def extendPalindrome(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count[0] += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        extendPalindrome(i, i+1)
        extendPalindrome(i, i)

    return count[0]

print(countSubstrings("abc"))
