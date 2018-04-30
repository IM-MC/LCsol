def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """

        letters = "abcdefghijklmnopqrstuvwxyz"
        indexes = []

        for char in letters:
            if s.count(char) == 1:
                indexes.append(s.index(char))

        return min(indexes) if len(indexes) > 0 else -1

print(firstUniqChar("loveleetcode"))
