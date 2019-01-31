def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    start = 0
    arr = []
    current = []
    backtrack(start,arr,current,nums)
    return arr

def backtrack(start, array, curr, nums):
    copy = list(curr)
    copy.sort()
    if copy not in array:
        array.append(copy)


    for i in range(start, len(nums)):
        curr.append(nums[i])
        backtrack(i+1,array,curr,nums)
        del curr[-1]

print(subsetsWithDup([1,2,2]))
