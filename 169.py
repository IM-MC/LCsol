def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = nums[0]
    count = 1

    for i in range(1,len(nums)):
        if count == 0:
            count += 1
            res = nums[i]
        elif res == nums[i]:
            count += 1
        else:
            count -= 1

    return res
