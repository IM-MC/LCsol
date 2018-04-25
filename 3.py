def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        chars = list(s)
        string = []
        maxString = []

        for char in chars:
            if char not in string:
                string.append(char)
            else:
                if len(string) > len(maxString):
                    maxString = list(string)
                while char in string:
                    string.pop(0)
                string.append(char)

            #print(string, maxString)

        if len(string) > len(maxString):
            maxString = list(string)

        return len(string) if len(maxString) == 0 else len(maxString)

string = "aab"

print(lengthOfLongestSubstring(string))
