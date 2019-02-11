def splitArray(arr):

    n = len(arr)
    wholeSum = rightSum = 0

    for num in arr:
        wholeSum += num

    for i in range(len(arr)-1, 0, -1):
        rightSum += arr[i]
        wholeSum -= arr[i]

        if rightSum == wholeSum:
            return True

    return False

print(splitArray([1,2,9,4,3,5]))
