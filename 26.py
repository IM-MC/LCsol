
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]

    return index + 1


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)
