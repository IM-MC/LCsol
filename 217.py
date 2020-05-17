def containsDuplicate(nums):
    dic = dict()

    for num in nums:
        if num in dic.keys():
            return True
        else:
            dic[num] = num


print(containsDuplicate([1, 2, 3, 1]))
