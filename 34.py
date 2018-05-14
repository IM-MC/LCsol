def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def divide(l, r):
        if nums[l] == target == nums[r]:
            return [l, r]

        if nums[l] <= target <= nums[r]:
            mid = l + (r-l)/2
            left_side = divide(l, mid)
            right_side = divide(mid+1, r)
            return max(left_side, right_side) if -1 in left_side+right_side else [left_side[0], right_side[1]]

        return [-1,-1]

    return divide(0, len(nums)-1)
