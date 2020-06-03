def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    ret = [1]*len(nums)
    check = 0

    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                ret[i] = max(ret[i], 1 + ret[j])

    return max(ret)


seq = [0,1,2,59,12,5,0,12]
print(lengthOfLIS(seq))