def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    j = 0

    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return j

print(removeElement([1,2,3,4], 3))
