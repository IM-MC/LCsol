def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums = sorted(nums)
    dp = [0]*len(nums)

    for i in range(len(nums)):
        for j in range(i, -1, -1):
            if (nums[i]%nums[j]==0):
                dp[i] = max(dp[i], dp[j]+1)
    
    maxIndex = 0
    for i in range(len(nums)):
        maxIndex = i if dp[i] > dp[maxIndex] else maxIndex

    res = []

    temp = nums[maxIndex]
    current = dp[maxIndex]
    for i in range(len(nums)-1,-1,-1):
        if (temp%nums[i] == 0 and dp[i] == current):
            res.append(nums[i])
            temp = nums[i]
            current -= 1

    return res

print(largestDivisibleSubset([3,4,16,8]))