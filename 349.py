def intersection(nums1, nums2):
    lookup = set()
    ret = []

    for num in nums1:
        lookup.add(num)

    for num in nums2:
        if num in lookup:
            ret.append(num)
            lookup.discard(num)

    return ret