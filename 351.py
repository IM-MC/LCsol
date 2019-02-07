def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    res = []

    def backtrack(curr, arr):
        if len(curr) == len(nums):
            temp = list(curr)
            res.append(temp)
            return

        for i in range(len(arr)):
            curr.append(arr[i])
            backtrack(curr, arr[:i] + arr[i+1:])
            del curr[-1]

    backtrack([], nums)

    return res

print(permuteUnique([1,2,2]))
