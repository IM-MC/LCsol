def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    left = prev = 0

    for i in range(len(nums)):
        left, prev = max(nums[i] + prev, left), left
        print(left,prev)

    return left

print(rob([2,1,1,1,1,1,1,1,1,1,1,1,1,10]))
