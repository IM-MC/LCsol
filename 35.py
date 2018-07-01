def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    index = 0

    if target in nums:
        return nums.index(target)
    else:
        for num in nums:
            if num > target:
                return index
            else:
                index += 1

        return index

print(searchInsert([1,3,5,7], 3))
