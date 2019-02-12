def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for num in nums:
        res = res^num

    return res

print(singleNumber([4,1,2,1,2,4,5]))
