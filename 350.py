def interesect(nums1, nums2):

    dic1 = {}
    dic2 = {}

    ret = []

    for num in nums1:
        if num not in dic1.keys():
            dic1[num] = 1
        else:
            dic1[num] += 1

    for num in nums2:
        if num not in dic2.keys():
            dic2[num] = 1
        else:
            dic2[num] += 1

    intersections = set(nums1).intersection(set(nums2))

    for num in intersections:
        ret.extend([num] * min(dic1[num], dic2[num]))

    return ret
