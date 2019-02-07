def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    arr = []

    for char in s:
        arr.append(int(char))

    if set(arr) == {0}:
        return 0

    if arr[len(arr)-1] == 0 and arr[len(arr)-2] > 2:
        return 0

    def findCombinations(arr):
        print(arr)
        if len(arr) == 0:
            return 1

        if arr[0] == 0:
            return 0

        if len(arr) == 1:
            return 1

        if arr[1] == 0 and arr[0] <= 2:
            return findCombinations(arr[2:])
        elif arr[0] >= 3:
            return findCombinations(arr[1:])
        elif arr[1] >= 7 and arr[0] >= 2:
            return findCombinations(arr[2:])
        else:
            return findCombinations(arr[1:]) + findCombinations(arr[2:])

    return findCombinations(arr)

print(numDecodings("27"))
