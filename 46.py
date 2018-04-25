def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    n = len(nums)
    curr = []
    array = []
    backtrack(nums, n, curr, array)
    return array

def backtrack(nums, n, curr, array):
    if (n == 0):
        array.append(list(curr))
        return

    for i in range(len(nums)):
        if nums[i] in curr:
            continue
        curr.append(nums[i])
        backtrack(nums, n-1, curr, array)
        del curr[-1]

print(permute([1,2,3]))
