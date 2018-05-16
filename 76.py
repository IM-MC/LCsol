import collections

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    need, missing = collections.Counter(t), len(t)

    start = end = i = 0

    for count, value in enumerate(s, 1):
        if need[value] > 0:
            missing -= 1

        need[value] -= 1
        print(need)
        if missing == 0:
            print(s[i], need[s[i]])
            while i < count and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not end or count - i <= end - start:
                start = i
                end = count

    return s[start:end]

print(minWindow("ADOBECODEBANC", "ABC"))
