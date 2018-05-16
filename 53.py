def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    curr_max = maximum = nums[0]

    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        maximum = max(curr_max, maximum)

    return maximum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
