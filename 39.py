def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    array = []
    curr = []
    value = 0
    backtrack(candidates, target, array, curr, value, 0)
    return(array)

def backtrack(candidates, target, array, curr, value, start):
    if value == target and curr not in array:
        arrayCopy = list(curr)
        array.append(arrayCopy)
        return

    for i in range(start,len(candidates)):
        if value+candidates[i] > target:
            continue
        curr.append(candidates[i])
        value += candidates[i]
        backtrack(candidates,target,array,curr,value, i)
        del curr[-1]
        value -= candidates[i]

print(combinationSum([2,3,6,7], 7))
