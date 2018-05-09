def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    arr = []

    def summary(nums, index, arr, string):
        if index+1 == len(nums) or nums[index+1] != nums[index] + 1:
            string += str(nums[index])
            del nums[index]
            arr.append(string)
            return

        if index == 0:
            string += str(nums[index]) + "->"
        summary(nums,index+1, arr, string)
        del nums[index]

    while len(nums) > 0:
        summary(nums, 0, arr, "")

    return arr

print(summaryRanges([0,2,3,4,6,8,9]))
