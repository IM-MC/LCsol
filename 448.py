def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    length = len(nums)
    array = []

    for i in range(length):
        value = abs(nums[i]) - 1
        if nums[value] > 0:
            nums[value] *= -1

    for i in range(length):
        if nums[i] > 0:
            array.append(i+1)


    return array

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
