class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '' or haystack == needle:return  0
        ne = len(needle)
        for k in range(len(haystack)-len(needle)+1):
            if haystack[k:ne+k] == needle:return k
        return -1
