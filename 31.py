def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    i = len(nums) - 1

    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i <= 0:
        nums.sort()
        return

    j = len(nums) - 1

    while nums[j] <= nums[i-1]:
        j -= 1

    temp = nums[i-1]
    nums[i-1] = nums[j]
    nums[j] = temp

    j = len(nums) - 1

    while i < j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
        j -= 1

    return

nums = [3,2,1]
nextPermutation(nums)
print(nums)
