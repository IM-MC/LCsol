def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    index = 0

    for num in nums:
        if index < 2 or num > nums[index-2]:
            nums[index] = num
            index += 1

    return index


print(removeDuplicates([1,1,1,2,3,3,4,5,5,5]))
