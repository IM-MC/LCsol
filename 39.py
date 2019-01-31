def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    array = []
    curr = []
    value = 0
    backtrack(candidates, target, value, curr, array,0)
    return(array)

# def backtrack(candidates, target, array, curr, value, start):
#     if value == target and curr not in array:
#         arrayCopy = list(curr)
#         array.append(arrayCopy)
#         return
#
#     for i in range(start,len(candidates)):
#         if value+candidates[i] > target:
#             continue
#         curr.append(candidates[i])
#         value += candidates[i]
#         backtrack(candidates,target,array,curr,value, i)
#         del curr[-1]
#         value -= candidates[i]


def backtrack(candidates, target, value, curr, array, start):
    print(curr)
    if value == target:
        listCopy = list(curr)
        array.append(listCopy)
        return

    for i in range(start, len(candidates)):
        if value + candidates[i] > target:
            continue

        curr.append(candidates[i])
        backtrack(candidates, target, value + candidates[i], curr, array,i)
        del curr[-1]

print(combinationSum([2,3,5], 8))
