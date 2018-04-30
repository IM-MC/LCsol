def longestPalindrome(s):
    substring = ""
    for i in range(0, len(s)):
        if i+1 < len(s):
            substring = helper(i, i+1, s, substring)
        substring = helper(i, i, s, substring)
    return substring

def helper(left, right, s, substring):
    new_sub = ""
    while(left >= 0 and right < len(s) and s[left] == s[right]):
        new_sub = s[left:right+1]
        left -= 1
        right += 1
    return new_sub if len(new_sub) > len(substring) else substring
