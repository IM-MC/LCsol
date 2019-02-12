def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    # "hacky" solution
    arr = s.split()
    arr.reverse()
    return ' '.join(map(str, arr))

    # 2 pointer
    left = 0
    arr = s.split()
    right = len(arr)-1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return ' '.join(map(str, arr))


print(reverseWords("the sky is blue"))
