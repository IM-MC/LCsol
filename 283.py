def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    # solution 1
    for num in nums:
        if num == 0:
            nums.remove(0)
            nums.append(0)

    return nums

    # 2 pointer

    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    for i in range(j, len(nums)):
        nums[i] = 0


print(moveZeroes([0, 1, 0, 3, 12]))
