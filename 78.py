def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    start = 0
    arr = list(list())
    current = []
    backtrack(start,arr,current,nums)
    return arr

def backtrack(start, array, curr, nums):
    copy = list(curr)
    array.append(copy)

    for i in range(start, len(nums)):
        curr.append(nums[i])
        backtrack(i+1,array,curr,nums)
        del curr[-1]


subsets([1,2,3])
