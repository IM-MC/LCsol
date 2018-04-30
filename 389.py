def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    for char in set(t):
        if t.count(char) > s.count(char):
            return char
